from ninja import Router
from typing import List
from core.models import ProductCategory, Product
from core.schemas.category import CategoryIn, CategoryOut
from django.shortcuts import get_object_or_404

api = Router()

@api.get('/category', response=List[CategoryOut])
def category_list(request):
    return ProductCategory.objects.all()

@api.get('/category/{category_id}', response=CategoryOut)
def category_detail(request, category_id: int):
    return get_object_or_404(ProductCategory, id=category_id)

@api.post("/category")
def category_create(request, payload: CategoryIn):
    category = payload.dict()
    ProductCategory.objects.create(**category)
    return category

@api.delete("/category/{category_id}")
def category_delete(request, category_id: int):
    category = get_object_or_404(ProductCategory, id=category_id)
    category.delete()
    return {"success": True}



