from ninja import ModelSchema
from ..models import User


class UserIn(ModelSchema):
    class Config:
        model = User
        model_fields = "__all__"

class UserOut(ModelSchema):
    class Config:
        model = User
        model_fields = "__all__"