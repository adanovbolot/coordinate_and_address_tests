import pytest
from data.data_test import open_file_coordinates_and_address, url_lat_lon, url_address
import allure


@allure.id('001')
@allure.title('Сравнить данные из адреса и координат')
@pytest.mark.parametrize('coordinates',
                         [open_file_coordinates_and_address('data/coordinates.json',
                          url_lat_lon(lat="-22.9519173", lon="-43.2104585"), 'data/coordinates.json')])
@pytest.mark.parametrize('address',
                         [open_file_coordinates_and_address('data/address.json',
                          url_address(address='Статуя Христа Искупителя'), 'data/address.json')])
def test_coordinates_and_address(coordinates, address):
    assert address == coordinates
    allure.dynamic.description(f"Должен вернуть широту, долготу и адрес: {coordinates, address} \nNICE")
