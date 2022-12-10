import requests
import json
import pytest
import os.path


def base_urls():
    return 'https://nominatim.openstreetmap.org/search.php?q=Большой+Сампсониевский+проспект%2C+41&format=jsonv2'


def read_file():
        with open('data/data.json', 'r') as json_file:
            return json.load(json_file)


def get_data_coordinates():
    response = requests.get(base_urls()).json()
    if os.path.exists('data/data.json') == True:
        return read_file()
    else:
        with open('data/data.json', 'w') as outfile:
            json.dump(response, outfile)
            return read_file()



# pprint.pp(get_data_coordinates())
