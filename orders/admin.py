from ast import Or
from django.contrib import admin
from .models import Order

# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['size', 'order_status', 'quantity', 'customer', 'created_at']
    list_filter = ['size', 'order_status', 'customer']

