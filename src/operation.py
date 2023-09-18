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

    def from_view(self):
        if 'Счет' in self.from_:
            return f"Счёт **{self.from_[-4:]} -> "
        elif self.from_ == "":
            return f""
        else:
            return f"{self.from_[0:-16]}{self.from_[-16:-12]} {self.from_[-12:-10]}** **** {self.from_[-4:]} -> "

    def to_view(self):
        if 'Счет' in self.to:
            return f"Счёт **{self.to[-4:]}"
        else:
            return f"{self.to[0:-16]}{self.to[-16:-12]} {self.to[-12:-10]}** **** {self.to[-4:]}"

    def __repr__(self):
        return (f'{self.date_view()} {self.description}\n'
                f'{self.from_view()}{self.to_view()}\n'
                f'{self.amount_view()}\n')

