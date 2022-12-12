# для запуска тестов

    git clone git@github.com:adanovbolot/coordinate_and_address_tests.git
    python -m venv myenv
    pip install -r requirements.txt
    source venv/bin/activate

Для запуска теста:
     
    pytest -s -v tests/test_api_get_location.py

# TESTCASE
test_coordinates_and_address

    идентификатор тест-кейса - 001
    Название - Сравнить данные из адреса и координат
    шаги - тест кейса
        Описание функции: open_file_coordinates_and_address
                принимает: file - который должен 
                                  прочитать данные из файла
                           url_lat_lon - принимает url с 
                                         которого нужно записать данные.
                                         Так же url_lat_lon принимает широту и долготу,
                                         для поиска место.
                           url_address - Так же принимает url, с параметрами адрес места.
         шаг - запрос на url - адреса и координат
         шаг - получить данные из url виде json
         шаг - создать файлы с данными виде json - адреса и координат
         шаг - если нет данных (open_file_coordinates_and_address)
               функция создает данные. 
         шаг - нужно передать параметры для координат и адреса
               (parametrize)
         шаг - поскольку данные правильные, но у координат и адресов есть различия в данных
               нужно получить данные по индексу, а именно 
                     display_name, lat, lon, place_id

    Ожидаемый результат - Сравнение координат и адреса
               allure - должен вернуть данные координат и адреса
                            PASSED


# Отчет Allure

    pytest --alluredir=allure-report/
    allure serve allure-report/
