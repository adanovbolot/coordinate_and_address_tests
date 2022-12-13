from data.data_test import open_file_coordinates_and_address, url_lat_lon, \
    url_address, get_example_coordinates, get_example_address
import pytest
import allure


@allure.id('001')
@pytest.mark.ADDRESS
@allure.title('Сравнить данные из адреса > координаты')
@pytest.mark.parametrize('address',
                         [open_file_coordinates_and_address('data/address.json',
                          url_address(address='Статуя Христа Искупителя'), 'data/address.json')
                          [0]['boundingbox']])
@pytest.mark.parametrize('example',
                         [get_example_coordinates()
                          ['boundingbox']])
def test_address(example, address):
    assert address == example
    allure.dynamic.description(f"Должен вернуть широту, долготу:\n "
                                f"Координаты: {example}\n"
                                f"Адрес: {address}" )


@allure.id('002')
@pytest.mark.COORDINATES
@allure.title('Сравнить данные из координат > адрес')
@pytest.mark.parametrize('coordinates',
                         [open_file_coordinates_and_address('data/coordinates.json',
                          url_lat_lon(lat="-22.9519173", lon="-43.2104585"), 'data/coordinates.json')['display_name']])
@pytest.mark.parametrize('example',
                         [get_example_address()
                          [0]['display_name']])
def test_coordinates(coordinates, example):
    assert coordinates == example
    allure.dynamic.description(f"Должен вернуть описание местности: "
                               f"Координаты: {coordinates}\n"
                               f"Адрес: {example}")

