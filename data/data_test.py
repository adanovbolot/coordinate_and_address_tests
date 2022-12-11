import requests
import json
import os.path
import csv


def url_lat_lon(lat=None, lon=None):
    return f"https://nominatim.openstreetmap.org" \
           f"/reverse.php?lat={lat}&lon={lon}&zoom=18&format=jsonv2"


def url_address():
    return f"https://nominatim.openstreetmap.org/search.php?q=Статуя+Христа-Искупителя&exclude_place_ids=56252671%2C541044&format=jsonv2"


def file_write(url, file_name):
    jsondata = requests.get(url).json()[0]
    # result = jsondata['display_name'], jsondata['lat'], jsondata['lon'], jsondata['place_id']
    result = jsondata['display_name'], jsondata['lat'], jsondata['lon'], jsondata['place_id']
    with open(file_name, 'w') as outfile:
        json.dump(result, outfile)
    # data_file = open(file_name, 'w', newline='')
    # csv_writer = csv.writer(data_file)
    # for data in jsondata:
    #     csv_writer.writerow(data.values())
    # data_file.close()
    # return data_file


def open_file_coordinates_and_address(file, url, file_name):
    if os.path.exists(file) == True:
        return csv.reader(file)
    else:
        file_write(url, file_name)
        return csv.reader(file)


# g = open_file_coordinates_and_address('data/address.json', url_address(), 'data/address.json')
# print(g)
