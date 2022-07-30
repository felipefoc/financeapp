from ninja import Router
from typing import List
from core.models import Bank
from core.schemas.bank import BankOut, BankIn
from django.shortcuts import get_object_or_404

api = Router()

@api.get('/bank', response=List[BankOut])
def banks_list(request):
    return Bank.objects.all()

@api.get('/bank/{bank_id}', response=BankOut)
def bank_detail(request, bank_id: int):
    return get_object_or_404(Bank, id=bank_id)

@api.post("/bank")
def bank_create(request, payload: BankIn):
    bank = payload.dict()
    Bank.objects.create(**bank)
    return bank

@api.delete("/bank/{bank_id}")
def bank_delete(request, bank_id: int):
    bank = get_object_or_404(Bank, id=bank_id)
    bank.delete()
    return {"success": True}

