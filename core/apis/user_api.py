from ninja import Router
from typing import List
from core.models import User
from core.schemas.user import UserOut, UserIn
from django.shortcuts import get_object_or_404

api = Router()

@api.get('/user', response=List[UserOut])
def user_list(request):
    return User.objects.all()

@api.get('/user/{user_id}', response=UserOut)
def user_detail(request, user_id: int):
    return get_object_or_404(User, id=user_id)

@api.post("/user")
def user_create(request, payload: UserIn):
    user = payload.dict()
    User.objects.create(**user)
    return user

@api.delete("/user/{user_id}")
def user_delete(request, user_id: int):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return {"success": True}