from ninja import ModelSchema
from ..models import Product


class ProductIn(ModelSchema):
    class Config:
        model = Product
        model_exclude = ["id"]

class ProductOut(ModelSchema):

    class Config:
        model = Product
        model_fields = "__all__"