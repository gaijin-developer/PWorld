from django.db import models

# Create your models here.
class Car (models.Model):
    brand=models.CharField(max_length=30)
    year=models.IntegerField(default=2023)

    def __str__(self):
        return f" your car is {self.brand} made in the year {self.year} "