import csv

def read_coords_files(files):
    """Función para leer multiples archivos .csv dentro del directorio addresses/ que contengan direcciones junto a sus coordenadas
    Args:
        files (list): lista de archivos csv
    Returns:
        coords (list): lista de coordenadas en formato (longitude, latitude)
        addresses (list): lista de direcciones
    """
    coords = []
    addresses = []
    for file in files:
        csv_file = "addresses/" + file
        with open(csv_file, encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                address = row[0]
                longitude = row[1]
                latitude = row[2]
                coords.append((longitude, latitude))
                addresses.append(address)
    return coords, addresses
