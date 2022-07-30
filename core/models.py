from django.db import models
from .choices import purchase, user

class User(models.Model):
    name = models.CharField(max_length=30)
    sex = models.IntegerField(choices=user.SEX_CHOICES)

    @property
    def is_male(self):
        if self.sex == 0:
            return True

    @property
    def is_female(self):
        if self.sex == 1:
            return True

class Bank(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return f'<Banco: {self.name}>'

class ProductCategory(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return f'<Categoria: {self.category}>'


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(ProductCategory, models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return f'<Produto: {self.name}>'


class Purchase(models.Model):
    product = models.ManyToManyField(Product)
    user = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField()
    bank = models.ForeignKey(Bank, models.SET_NULL, null=True, blank=True)
    kind = models.IntegerField(choices=purchase.KIND_CHOICES)
    installments = models.IntegerField(blank=True, null=True)
    month = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<Banco: {self.bank.name} | {self.kind}>'

    @property
    def is_credit(self):
        if self.kind == purchase.KIND_CHOICES[0]:
            return True

    @property
    def is_debit(self):
        if self.kind == purchase.KIND_CHOICES[1]:
            return True

    @property
    def total(self):
        p = self.product.all()
        return sum([i.price for i in p])