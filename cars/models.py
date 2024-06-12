from django.db import models
from brands.models import Brand
# Create your models here.

def brand_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / brand_<brand_name>/<filename>
    return 'brand_{0}/{1}'.format(instance.brand.brand_name, filename)

class Car(models.Model):
    img = models.ImageField(upload_to=brand_directory_path)
    car_model = models.CharField(max_length=150)
    brand = models.ForeignKey(to=Brand, on_delete=models.CASCADE, related_name = 'cars')
    quantity = models.IntegerField()
    describtion=models.TextField()
    price = models.FloatField()
    slug = models.SlugField(max_length=250, unique=True, blank=True, null=True)
    def __str__(self):
        return self.car_model