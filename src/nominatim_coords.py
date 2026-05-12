import csv
import time
from geopy.geocoders import Nominatim

def search_coords(addr):
    """Dada una dirección en formato string, devuelve una sus coordenadas en formato (longitude, latitude)"""
    geolocator = Nominatim(user_agent="prueba_OR-Tools")
    try:
        # Nominatim requiere 1 segundo entre peticiones para ser gratis
        time.sleep(1.1)
        location = geolocator.geocode(addr)

        if location:
            # OSRM necesita [longitud, latitud]
            return location.longitude, location.latitude
        else:
            print(f"No se pudo encontrar: {addr}")
    except Exception as e:
        print(f"Error procesando {addr}: {e}")

    return None


def write_in_csv(file, coords_list, addresses_lists):
    route = "addresses/" + file
    with open(route, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=",", quoting=csv.QUOTE_ALL)

        for text, (long, lat) in zip(addresses_lists, coords_list):
            writer.writerow([text, long, lat])

def save_coords_nominatim(addresses_lists, address_files):
    """Recibe un diccionario donde las claves son los archivos csv y los valores son listas con las direcciones que corresponden al archivo.
    Para cada dirección busca sus coordenadas y las guarda en el archivo csv correspondiente.
    Devuelve dos listas, una con las direcciones válidas y otra con las coordenadas"""
    valid_coords = []
    processed_addresses = []

    for file in address_files:
        address_list = addresses_lists[file]
        valid_coords_file = []
        processed_addresses_file = []

        for addr in address_list:
            location = search_coords(addr)
            if location:
                valid_coords.append(location)
                valid_coords_file.append(location)
                processed_addresses_file.append(addr)
                processed_addresses.append(addr)

        write_in_csv(file, valid_coords_file, processed_addresses_file)

    return processed_addresses, valid_coords
