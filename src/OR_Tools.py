from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

DISTANCE_SPAN = 5

def create_routes(data):
    """Data es un diccionario que contiene:
        - Matriz de distancias
        - Los vehículos disponibles
        - El índice del depósito/punto de partida"""

    # El manager es el traductor entre el algoritmo de OR-Tools y el problema a resolver.
    # El modelo crea nodos intermedios según necesite.
    # Ej.: el manager se encarga de saber que el nodo 0 en la matriz, es el nodo 19 en el modelo
    manager = pywrapcp.RoutingIndexManager(len(data["distance_matrix"]), len(data["vehicles"]), data["depot"])

    # Instancia el modelo encargado de armar las rutas.
    routing = pywrapcp.RoutingModel(manager)

    # Agregamos la dimensión de distancia.
    add_distance_dimension(routing, manager, data["distance_matrix"])

    add_orders_limit(routing, data["distance_matrix"], len(data["vehicles"]))


    # Buscamos una primera solución, este caso PATH_CHEAPEST_ARC usa un algoritmo greedy, yendo al nodo más cercano
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )

    # Resolvemos
    solution = routing.SolveWithParameters(search_parameters)

    if solution:
        return get_routes(data, routing, manager, solution)
    return None


def add_distance_dimension(routing, manager, distance_matrix):
    # Transit callback es una función que se va a utilizar para decirle al modelo cuanto cuesta ir de un punto a otro.
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return int(distance_matrix[from_node][to_node])

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Definimos al modelo que el costo a tener en cuenta es la distancia, buscando minimizarla.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Definimos una distancia máxima a recorrer, para esta primera iteración no tenemos restricción
    max_distance = sum_distances(distance_matrix)

    # Agregamos la dimensión de distancia.
    dimension_name = "Distance"
    routing.AddDimension(
        transit_callback_index, #Función que calcula las distancias
        0,  # No slack. El slack es un valor que se suma extra cada vez que se llega a un nodo
        max_distance,  # Máxima distancia por vehículo
        True,  # todos los vehículos arrancan en 0
        dimension_name,
    )
    distance_dimension = routing.GetDimensionOrDie(dimension_name)

    # Global span busca equilibrar las distancias recorridas por los vehículos
    # Multiplica la diferencia entre el vehículo con más distancia y el que menos por el valor dado y lo suma como coste extra
    # A VERIFICAR QUÉ VALOR USAR. SI ES MUY CHICO NO EQUILIBRA, SI ES MUY GRANDE PUEDE HACER RUTAS MALAS.
    distance_dimension.SetGlobalSpanCostCoefficient(DISTANCE_SPAN)

def add_orders_limit(routing, distance_matrix, num_vehicles):
    # Creamos una dimensión de "Contador" de paradas.
    def demand_callback(from_index):
        # Cada parada cuenta como 1 unidad de carga
        return 1

    demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)

    # Un vehículo no puede llevar todos los pedidos, buscamos que todos lleven similar cantidad con un margen de +-
    order_per_vehicles = round((len(distance_matrix) / num_vehicles) * 1.5)

    routing.AddDimension(
        demand_callback_index,
        0,  # sin slack.
        int(order_per_vehicles),  # MÁXIMO de pedidos por camión (ajusta este número según tu necesidad)
        True,
        "Capacidad"
    )

def sum_distances(distance_matrix):
    return int(sum(sum(row) for row in distance_matrix))

def get_routes(data, routing, manager, solution):
    routes  = []
    for vehicle in data["vehicles"]:
        actual_route = []
        index = routing.Start(vehicle)

        while not routing.IsEnd(index):
            # Traducimos el índice interno al nodo original de la matriz
            node_index = manager.IndexToNode(index)
            actual_route.append(node_index)

            # Pasamos al siguiente punto de la ruta
            index = solution.Value(routing.NextVar(index))

        # Añadimos el último nodo (el regreso al depósito)
        actual_route.append(manager.IndexToNode(index))

        # Guardamos la ruta de este vehículo en nuestra lista maestra, descartando el depósito
        routes.append(actual_route[1:-1])
    return routes
