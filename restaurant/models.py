# restaurant/models.py
from django.db import models


# Create your models here.

class MyTopping(models.Model):
    class Meta:
        db_table = "my_topping"

    def __str__(self):
        return self.topping_name

    topping_name = models.CharField(max_length=100)


class MyPizza(models.Model):
    class Meta:
        db_table = "my_pizza"

    def __str__(self):
        return self.pizza_name

    pizza_name = models.CharField(max_length=100)
    pizza_topping = models.ManyToManyField(MyTopping)