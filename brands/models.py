from django.db import models

# Create your models here.
class Brand(models.Model):
    brand_name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    def __str__(self) -> str:
        return f'{self.brand_name}'