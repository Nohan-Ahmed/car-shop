from django.db import models
from django.contrib.auth.models import User
from cars.models import Car
# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
    car = models.ForeignKey(to=Car, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    total = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # Check if this is a new order
            if self.car.quantity >= self.quantity:
                self.total = self.car.price * self.quantity
                self.car.quantity -= self.quantity
                self.car.save()  # Save the updated car quantity
            else:
                raise Exception("Not enough stock available for the requested car.")
        super().save(*args, **kwargs)
        
    def __str__(self) -> str:
        return f'Order id - {self.pk}'
