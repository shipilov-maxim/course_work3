import json
from pathlib import Path
from src.operation import Operation

JSON_FILE = Path(__file__).resolve().parent.parent / 'operations.json'


def load_json(file_path):
    with open(file_path, encoding="utf-8") as f:
        return json.load(f)


def sort_data(data_):
    sorted_data = sorted(data_, key=lambda x: x.get('date'), reverse=True)
    return sorted_data


def clear_data(data_):
    clear_data = []
    for item in data_:
        try:
            if item['state'] == "EXECUTED":
                try:
                    item['from'] *= 1
                except KeyError:
                    item['from'] = ""
                    clear_data.append(item)
        except KeyError:
            pass
    return clear_data


def list_class(list):
    list_class = []
    for operation in list:
        list_class.append(Operation(operation['id'],
                                    operation['state'],
                                    operation['date'],
                                    operation['operationAmount'],
                                    operation['description'],
                                    operation['from'],
                                    operation['to'])
                          )
    return list_class
