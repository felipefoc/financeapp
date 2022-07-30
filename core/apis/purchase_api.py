from ninja import Router
from typing import List
from core.models import Purchase, User, Bank, Product
from core.schemas.purchase import PurchaseOut, PurchaseIn
from django.shortcuts import get_object_or_404

api = Router()

@api.get('/purchase', response=List[PurchaseOut])
def purchase_list(request):
    return Purchase.objects.all()

@api.get('/purchase/{purchase_id}', response=PurchaseOut)
def purchase_detail(request, purchase_id: int):
    return get_object_or_404(Purchase, id=purchase_id)

@api.post("/purchase")
def purchase_create(request, payload: PurchaseIn):
    purchase = payload.dict()
    user = User.objects.get(id=purchase['user'])
    bank = Bank.objects.get(id=purchase['bank'])
    products = Product.objects.filter(id__in=purchase['product'])
    instance = Purchase.objects.create(
        user=user,
        quantity=purchase['quantity'],
        bank=bank,
        kind=purchase['kind'],
        installments=purchase['installments']
    )
    for p in products:
        instance.product.add(p)
    instance.save()
    return {"message": "ok"}

@api.delete("/purchase/{purchase_id}")
def purchase_delete(request, purchase_id: int):
    purchase = get_object_or_404(Purchase, id=purchase_id)
    purchase.delete()
    return {"success": True}


