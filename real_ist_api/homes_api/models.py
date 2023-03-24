from django.db import models

# Create your models here.
class Home(models.Model):
    houseNum = models.IntegerField()
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.IntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    bedroom = models.IntegerField()
    bathroom = models.IntegerField()
    description = models.TextField()
    squareFeet = models.IntegerField()
    image = models.ImageField()
    