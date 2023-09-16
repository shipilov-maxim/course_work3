import json
from pathlib import Path

JSON_FILE = Path(__file__).resolve().parent.parent / 'operations.json'


def load_json(file_path):
    with open(file_path, encoding="utf-8") as f:
        return json.load(f)


class Operation:

    def __init__(self, id_, state, date, operation_amount, description, from_, to):
        self.id_ = id_
        self.state = state
        self.date = date
        self.operation_amount = operation_amount
        self.description = description
        self.from_ = from_
        self.to = to

    def is_executed(self):
        if self.state == "EXECUTED":
            return True

    def date_view(self):
        date = self.date[:10]
        date = date[8:10]+ "." + date[5:7] + "." + date[:4]
        return f"{date}"

    def amount_view(self):
        return f"{self.operation_amount['amount']} {self.operation_amount['currency']['name']}"

    def account_view(self, account):
        if 'Счет' in account:
            return f"Счёт **{account[-4:]}"
        else:
            return f"{account[0:-16]}{account[-16:-12]} {account[-12:-10]}** **** {account[-4:]}"

    def __repr__(self):
        return (f'{self.date_view()} {self.description}\n'
                f'{self.account_view(self.from_)} -> {self.account_view(self.to)}\n'
                f'{self.amount_view()}\n')


def sort_data(data_):
    dataa = {x for x in data_ if x['date'] is not None}
    sorted_data = sorted(dataa, key=lambda x: x.get('date'), reverse=True)
    return sorted_data


list_clas_op = []
# data = load_json(JSON_FILE)
# sorted_dat = sort_data(data)

for operation in load_json(JSON_FILE):
    try:
        list_clas_op.append(Operation(operation['id'],
                                      operation['state'],
                                      operation['date'],
                                      operation['operationAmount'],
                                      operation['description'],
                                      operation['from'],
                                      operation['to'])
                            )
    except KeyError:
        pass

o = list_clas_op[0:]

for i in o:
    if i.is_executed():
        print(i)

