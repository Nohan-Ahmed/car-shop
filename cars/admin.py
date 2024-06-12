from django.contrib import admin
from . import models
# Register your models here.
class CustomCarAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('car_model',)}
    list_display = ['car_model', 'brand', 'quantity', 'price']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'date', 'car']
admin.site.register(models.Car, CustomCarAdmin)
admin.site.register(models.Comment, CommentAdmin)