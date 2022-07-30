from ninja import Schema

class BankOut(Schema):
    id: int
    name: str

class BankIn(Schema):
    name: str