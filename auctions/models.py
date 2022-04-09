from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class List(models.Model):
    name = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}: {self.create_date}"


class Bid(models.Model):
    price = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    list = models.ForeignKey(List, on_delete=models.CASCADE)

    def __str__(self):
        return f"price:{self.price}"
