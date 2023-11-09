import json

import pytest

from src.functions import card_number, date_converter, filtering_sorting_list, getting_data_from_file


def test_getting_data_from_file():
    # Создание временного файла с данными для теста
    temp_data = [
        {"name": "Mary", "age": 28},
        {"name": "Artem", "age": 38}]
    with open("temp_data.json", "w") as file:
        json.dump(temp_data, file)
    result = getting_data_from_file("temp_data.json")
    assert result == temp_data


@pytest.mark.parametrize("test_input, expected", [([{'state': 'EXECUTED', 'date': '2022-01-01'},
                                                    {'state': 'EXECUTED', 'date': '2022-01-02'},
                                                    {'state': 'EXECUTED', 'date': '2022-01-03'}],
                                                   [{'state': 'EXECUTED', 'date': '2022-01-01'},
                                                    {'state': 'EXECUTED', 'date': '2022-01-02'},
                                                    {'state': 'EXECUTED', 'date': '2022-01-03'}]),
                                                  ([{'state': 'PENDING', 'date': '2022-01-01'},
                                                    {'state': 'EXECUTED', 'date': '2022-01-02'},
                                                    {'state': 'EXECUTED', 'date': '2022-01-03'},
                                                    {'state': 'PENDING', 'date': '2022-01-04'},
                                                    {'state': 'EXECUTED', 'date': '2022-01-05'}],
                                                   [{'state': 'EXECUTED', 'date': '2022-01-02'},
                                                    {'state': 'EXECUTED', 'date': '2022-01-03'},
                                                    {'state': 'EXECUTED', 'date': '2022-01-05'}])])
def test_filtering_sorting_list(test_input, expected):
    assert filtering_sorting_list([]) == []
    assert filtering_sorting_list(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [("VISA 1234 5678 9012 3456", "VISA 1234 56** **** 3456"),
                                                 ("счет 12345678901234567890", "счет **7890")])
def test_card_number(test_input, expected):
    assert card_number(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [("2019-08-26T10:50:58.294041", '26-08-2019')])
def test_date_converter(test_input, expected):
    assert date_converter(test_input) == expected
