from ninja import ModelSchema
from ..models import ProductCategory


class CategoryIn(ModelSchema):
    class Config:
        model = ProductCategory
        model_exclude = ["id"]

class CategoryOut(ModelSchema):
    class Config:
        model = ProductCategory
        model_fields = "__all__"