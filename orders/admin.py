from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer','car','quantity', 'order_date', 'total']
    readonly_fields = ('total',)
