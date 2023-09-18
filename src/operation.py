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
            return f"Счёт **{account[-4:]} -> "
        elif account == "":
            return f""
        else:
            return f"{account[0:-16]}{account[-16:-12]} {account[-12:-10]}** **** {account[-4:]} -> "

    def __repr__(self):
        return (f'{self.date_view()} {self.description}\n'
                f'{self.account_view(self.from_)}{self.account_view(self.to)}\n'
                f'{self.amount_view()}\n')

