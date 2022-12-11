import pytest
from data.data_test import open_file_coordinates_and_address, url_lat_lon, url_address
import allure


@pytest.mark.parametrize('coordinates',
                         [open_file_coordinates_and_address('data/coordinates.json',
                          url_lat_lon(lat="-22.9519173", lon="-43.2104585"), 'data/coordinates.json')])
@pytest.mark.parametrize('address',
                         [open_file_coordinates_and_address('data/address.json',
                          url_address(), 'data/address.json')])
def test_data(coordinates, address):
    assert address == coordinates


# @allure.id('001')
# @allure.title('Протестировать с адреса координаты')
# @pytest.mark.ADDRESS
# @pytest.mark.parametrize('example_lat', ['59.96841475'])
# @pytest.mark.parametrize('example_lon', ['30.342996143752842'])
# def test_get_data_from_address_and_compare_coordinates(base_url, example_lat, example_lon):
#     response = requests.get(base_url + LINK_VIA_ADDRESS)
#     list_result = response.json()
#     result = next((item for item in list_result if item))
#     assert response.status_code == int(200), f"ВЕРНУЛ: {response.status_code}"
#     assert [result['lat'], result['lon']] == [example_lat, example_lon]
#     allure.dynamic.description(f"Должен вернуть широту, долготу: {[result['lat'], result['lon']]}\nNICE" )
#
#
# @allure.id('002')
# @allure.title('Протестировать с координат адрес')
# @pytest.mark.COORDINATES
# @pytest.mark.parametrize('example', [{'house_number': '29 к1', 'road': 'Выборгская набережная',
#                                       'city_district': 'округ Сампсониевское', 'city': 'Санкт-Петербург',
#                                       'ISO3166-2-lvl15': 'RU-SPE', 'state': 'Санкт-Петербург',
#                                       'ISO3166-2-lvl4': 'RU-SPE', 'region': 'Северо-Западный федеральный округ',
#                                       'postcode': '194044', 'country': 'Россия', 'country_code': 'ru'}])
# def test_get_data_from_coordinates_and_compare_address(base_url, example):
#     response = requests.get(base_url + LINK_VIA_COORDINATES)
#     list_result = response.json()
#     assert response.status_code == int(200), f"ВЕРНУЛ: {response.status_code}"
#     assert list_result['address'] == example
#     allure.dynamic.description(f"Должен вернуть данные из json адреса: {list_result['address']}\nNICE")
