from OR_Tools import create_routes
from csv_coords import read_coords_files
from src.nominatim_coords import save_coords_nominatim
import requests

addresses_dict = {"castelar.csv": ["Arias 2340, Castelar, Buenos Aires, Argentina",
                                    "Carlos Casares 950, Castelar, Buenos Aires, Argentina",
                                    "Santa Rosa 1210, Castelar, Buenos Aires, Argentina",
                                    "Rodríguez Peña 820, Castelar, Buenos Aires, Argentina",
                                    "España 415, Castelar, Buenos Aires, Argentina",
                                    "Timbúes 1530, Castelar, Buenos Aires, Argentina",
                                    "Zapiola 2100, Castelar, Buenos Aires, Argentina",
                                    "Av. Rivadavia 20100, Castelar, Buenos Aires, Argentina"],
                    "ituzaingo.csv": ["José María Paz 1100, Ituzaingó, Buenos Aires, Argentina",
                                    "Bacacay 740, Ituzaingó, Buenos Aires, Argentina",
                                    "Brandsen 2250, Ituzaingó, Buenos Aires, Argentina",
                                    "Mariano Acosta 155, Ituzaingó, Buenos Aires, Argentina",
                                    "Olazábal 890, Ituzaingó, Buenos Aires, Argentina",
                                    "Pirán 1020, Ituzaingó, Buenos Aires, Argentina",
                                    "General Mansilla 630, Ituzaingó, Buenos Aires, Argentina",
                                    "Fragata Sarmiento 1415, Ituzaingó, Buenos Aires, Argentina"],
                    "moron.csv":    ["Almirante Brown 720, Morón, Buenos Aires, Argentina",
                                    "Nuestra Señora del Buen Viaje 950, Morón, Buenos Aires, Argentina",
                                    "General Machado 1120, Morón, Buenos Aires, Argentina",
                                    "Sarmiento 480, Morón, Buenos Aires, Argentina",
                                    "Agüero 1350, Morón, Buenos Aires, Argentina",
                                    "Belgrano 210, Morón, Buenos Aires, Argentina",
                                    "San Martín 340, Morón, Buenos Aires, Argentina"],
                    "san_isidro.csv":["Av. del Libertador 16300, San Isidro, Buenos Aires, Argentina",
                                    "Belgrano 420, San Isidro, Buenos Aires, Argentina",
                                    "Chacabuco 150, San Isidro, Buenos Aires, Argentina",
                                    "Dardo Rocha 2100, San Isidro, Buenos Aires, Argentina",
                                    "Diego Palma 780, San Isidro, Buenos Aires, Argentina",
                                    "Juan Segundo Fernández 1240, San Isidro, Buenos Aires, Argentina",
                                    "Roque Sáenz Peña 910, San Isidro, Buenos Aires, Argentina"],
                    "lanus.csv":    ["Avenida Hipólito Yrigoyen 4500, Lanús, Buenos Aires, Argentina",
                                    "25 de Mayo 120, Lanús, Buenos Aires, Argentina",
                                    "Ituzaingó 1550, Lanús, Buenos Aires, Argentina",
                                    "Basavilbaso 1900, Lanús, Buenos Aires, Argentina",
                                    "Margarita Weild 1300, Lanús, Buenos Aires, Argentina",
                                    "Oncativo 1400, Lanús, Buenos Aires, Argentina",
                                    "General Arias 1800, Lanús, Buenos Aires, Argentina",
                                    "Anatole France 1600, Lanús, Buenos Aires, Argentina",
                                    "Eva Perón 2500, Lanús, Buenos Aires, Argentina",
                                    "Sarmiento 1100, Lanús, Buenos Aires, Argentina"],
                    "quilmes.csv":  ["Rivadavia 150, Quilmes, Buenos Aires, Argentina",
                                    "Alvear 600, Quilmes, Buenos Aires, Argentina",
                                    "Mitre 550, Quilmes, Buenos Aires, Argentina",
                                    "Videla 200, Quilmes, Buenos Aires, Argentina",
                                    "Garibaldi 300, Quilmes, Buenos Aires, Argentina",
                                    "Humberto Primo 150, Quilmes, Buenos Aires, Argentina",
                                    "Olavarría 250, Quilmes, Buenos Aires, Argentina",
                                    "Avenida Centenario 1200, Quilmes, Buenos Aires, Argentina",
                                    "Brandsen 400, Quilmes, Buenos Aires, Argentina",
                                    "Moreno 700, Quilmes, Buenos Aires, Argentina"],
                    "la_matanza.csv":["Avenida de Mayo 200, Ramos Mejía, Buenos Aires, Argentina",
                                    "Arieta 2200, San Justo, Buenos Aires, Argentina",
                                    "Villegas 2400, San Justo, Buenos Aires, Argentina",
                                    "Rosales 300, Ramos Mejía, Buenos Aires, Argentina",
                                    "Necochea 150, Ramos Mejía, Buenos Aires, Argentina",
                                    "Almafuerte 3100, San Justo, Buenos Aires, Argentina",
                                    "Hipólito Yrigoyen 2600, San Justo, Buenos Aires, Argentina",
                                    "Alsina 50, Ramos Mejía, Buenos Aires, Argentina",
                                    "Entre Ríos 2900, San Justo, Buenos Aires, Argentina",
                                    "Mariano Moreno 400, Ramos Mejía, Buenos Aires, Argentina"],
                    "palermo.csv":  ["Avenida Santa Fe 3200, Palermo, CABA, Argentina",
                                    "Honduras 5100, Palermo, CABA, Argentina",
                                    "Gurruchaga 1800, Palermo, CABA, Argentina",
                                    "Thames 2100, Palermo, CABA, Argentina",
                                    "Gorriti 4800, Palermo, CABA, Argentina",
                                    "Malabia 1900, Palermo, CABA, Argentina",
                                    "Fitz Roy 1600, Palermo, CABA, Argentina",
                                    "Bonpland 1700, Palermo, CABA, Argentina",
                                    "Avenida del Libertador 3500, Palermo, CABA, Argentina",
                                    "Jerónimo Salguero 2400, Palermo, CABA, Argentina"],
                    "caballito.csv":["Avenida Rivadavia 5100, Caballito, CABA, Argentina",
                                    "Rosario 600, Caballito, CABA, Argentina",
                                    "Yerbal 800, Caballito, CABA, Argentina",
                                    "Avenida La Plata 300, Caballito, CABA, Argentina",
                                    "Acoyte 150, Caballito, CABA, Argentina",
                                    "Formosa 250, Caballito, CABA, Argentina",
                                    "Hidalgo 600, Caballito, CABA, Argentina",
                                    "Avenida José María Moreno 400, Caballito, CABA, Argentina",
                                    "Neuquén 1100, Caballito, CABA, Argentina",
                                    "Donato Álvarez 500, Caballito, CABA, Argentina"]
                  }


def main():
    data, addresses = create_data_model(addresses_dict, addresses_dict.keys(),False)

    solution = create_routes(data)
    if solution:
        for i, route in enumerate(solution):
            print(f"El vehiculo {i} recorre {len(route)} paradas")
            addrs = [addresses[a] for a in route]
            print(f"Vehículo {i}: {' -> '.join(addrs)}")
    else:
        print("No se pudo encontrar una solucion")

def create_data_model(addresses_dct, files_names, inet):
    data = {}

    #Elegimos de donde cargar los datos, si desde nominatim o desde algún archivo csv
    if not inet:
        coords, addresses = read_coords_files(files_names)
    else:
        addresses, coords = save_coords_nominatim(addresses_dct, files_names)

    distance_matrix = generate_matrix(coords)

    data["distance_matrix"] = distance_matrix
    data["vehicles"] = [0,1,2,3,4]
    data["depot"] = 0
    return data, addresses

def generate_matrix(coords):
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

if __name__ == "__main__":
    main()