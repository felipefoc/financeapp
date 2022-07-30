from ninja import ModelSchema
from ..models import Purchase


class PurchaseIn(ModelSchema):
    class Config:
        model = Purchase
        model_exclude = ["id", "month"]

class PurchaseOut(ModelSchema):
    class Config:
        model = Purchase
        model_fields = "__all__"