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
    Название - Протестировать с адреса координаты
    шаги - тест кейса
        1 шаг - Открыть главный URL
        2 шаг - В search отправить
          запрос по адресу: выборгская, санкт-петербург,
          большой сампсониевский проспект, в json формате
        3 шаг - Полученные данные изменить в json
        4 шаг - Пройтись циклом по списку
        5 шаг - Проверка статус кода
        6 шаг - Из списка получить широту 
        7 шаг - Из списка получить долготу
    Ожидаемый результат - 1. Получить статус код - 200
                          2. Сравнение координат
                            PASSED


# Отчет Allure

    pytest --alluredir=allure-report/
    allure serve allure-report/
