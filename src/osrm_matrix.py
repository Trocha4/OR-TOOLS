import requests

def generate_distance_matrix(coords):
    """A partir de una lista de coordenadas (long, lat) realiza una consulta a OSRM para obtener la matriz de distancias

    Args:
        coords (list): lista de coordenadas (long, lat)

    Returns:
        distance_matrix (list): matriz de distancias. Matriz[i][j] refiere a la distancia del punto i al punto j
    """
    # Armamos el request a OSRM para armar la matriz de distancias
    string_coords = ";".join([f"{c[0]},{c[1]}" for c in coords])
    url = f"http://router.project-osrm.org/table/v1/driving/{string_coords}?annotations=distance"

    try:
        response = requests.get(url).json()
        if response.get('code') == 'Ok':
            matriz = response['distances']
            return matriz
        else:
            return f"Error de OSRM: {response.get('code')}"

    except Exception as e:
        return f"Error de conexión con el servidor de rutas: {e}"
