from ninja import Router
from typing import List
from core.models import Product, ProductCategory
from core.schemas.product import ProductOut, ProductIn
from django.shortcuts import get_object_or_404

api = Router()

@api.get('/product', response=List[ProductOut])
def product_list(request):
    return Product.objects.all()

@api.get('/product/{product_id}', response=ProductOut)
def product_detail(request, product_id: int):
    return get_object_or_404(Product, id=product_id)

@api.post("/product")
def product_create(request, payload: ProductIn):
    product = payload.dict()
    product['category'] = ProductCategory.objects.get(id=product['category'])
    p = Product.objects.create(**product)
    return {"data": p.id}

@api.delete("/product/{product_id}")
def product_delete(request, product_id: int):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return {"success": True}


