import requests
import json
import os.path
import csv


def url_lat_lon(lat=None, lon=None):
    return f"https://nominatim.openstreetmap.org" \
           f"/reverse.php?lat={lat}&lon={lon}&zoom=18&format=jsonv2"


def url_address(address):
    url = f"https://nominatim.openstreetmap.org/search.php?q={address}&exclude_place_ids=56252671%2C541044&format=jsonv2"
    split_url = url.split()
    return '+'.join(split_url)


def file_write(url, file_name):
    jsondata = requests.get(url).json()
    with open(file_name, 'w', encoding='utf8') as outfile:
        return json.dump(jsondata, outfile, ensure_ascii=False)


def open_file_coordinates_and_address(file, url, file_name):
    if os.path.exists(file) == True:
        with open(file) as f:
            return json.load(f)
    else:
        file_write(url, file_name)
        with open(file) as f:
            return json.load(f)


def get_example_coordinates():
    return open_file_coordinates_and_address('data/example_coordinates.json', url_lat_lon(
        lat="-22.9519173", lon="-43.2104585"), 'data/example_coordinates.json')


def get_example_address():
    return open_file_coordinates_and_address('data/example_address.json', url_address('Статуя Христа Искупителя'), 'data/example_address.json')

