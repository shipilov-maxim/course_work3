import json
import pytest
from pathlib import Path
import sys
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, BASE_DIR.__str__())
from src.utils import load_json, sort_data, clear_data, list_class
from src.operation import Operation


@pytest.fixture
def json_data(tmp_path):
    data = [
        {"id": 1, "date": "2019-04-18T11:22:18.800453"},
        {"id": 1, "date": "2019-11-13T17:38:04.800051"},
        {"id": 1, "date": "2019-10-13T17:38:04.800051"}
    ]

    path = tmp_path / "test_data.json"

    with open(path, "w") as test_data:
        test_data.write(json.dumps(data))

    return path


def test_load_json(json_data):
    data = load_json(json_data)

    assert list(data) == [
        {"id": 1, "date": "2019-04-18T11:22:18.800453"},
        {"id": 1, "date": "2019-11-13T17:38:04.800051"},
        {"id": 1, "date": "2019-10-13T17:38:04.800051"}
    ]


def test_sort_data():
    list_ = [
        {"id": 1, "date": "2019-04-18T11:22:18.800453"},
        {"id": 1, "date": "2019-11-13T17:38:04.800051"},
        {"id": 1, "date": "2019-10-13T17:38:04.800051"}
    ]
    data = sort_data(list_)

    assert list(data) == [
        {"id": 1, "date": "2019-11-13T17:38:04.800051"},
        {"id": 1, "date": "2019-10-13T17:38:04.800051"},
        {"id": 1, "date": "2019-04-18T11:22:18.800453"}
    ]


def test_clear_data():
    list_ = [{'state': "EXECUTED", 'from': "2019-04-18T11:22:18.800453"}]
    list_canceled = [{}]
    list_from = [{'state': "EXECUTED"}]
    data = clear_data(list_)
    assert list(data) == [{'from': '2019-04-18T11:22:18.800453', 'state': 'EXECUTED'}]
    data = clear_data(list_canceled)
    assert list(data) == []
    data = clear_data(list_from)
    assert list(data) == [{'from': '', 'state': 'EXECUTED'}]


def test_list_class():
    list_ = [
        {
            "id": 482520625,
            "state": "EXECUTED",
            "date": "2019-11-13T17:38:04.800051",
            "operationAmount": {
                "amount": "62814.53",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 38611439522855669794",
            "to": "Счет 46765464282437878125"
        },
        {
            "id": 414894334,
            "state": "EXECUTED",
            "date": "2019-06-30T15:11:53.136004",
            "operationAmount": {
                "amount": "95860.47",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 59956820797131895975",
            "to": "Счет 43475624104328495820"
        },
        {
            "id": 509552992,
            "state": "EXECUTED",
            "date": "2019-04-19T12:02:30.129240",
            "operationAmount": {
                "amount": "81513.74",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Maestro 9171987821259925",
            "to": "МИР 2052809263194182"
        }
    ]
    data = list_class(list_)

    assert data == [Operation(*operation.values()) for operation in list_]

