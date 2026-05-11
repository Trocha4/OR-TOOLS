import csv

def read_coords_files(files):
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