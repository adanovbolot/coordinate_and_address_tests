import pytest
import requests

from data.data_test import get_data_coordinates
# import allure


@pytest.mark.parametrize('data', get_data_coordinates())
def test_test(data):
    assert data == 'stop', data


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
