from django.contrib import admin
from .models import MyTopping, MyPizza

# Register your models here.

admin.site.register(MyPizza)
admin.site.register(MyTopping)