from django.db import models
from django.conf import settings

class Store(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.TextField(max_length=100)
    is_franchise = models.TextField(max_length=250)


class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.TextField(max_length=100)
    amount = models.IntegerField()
    price = models.IntegerField()
    adult = models.IntegerField()

