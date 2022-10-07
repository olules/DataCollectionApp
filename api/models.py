from unittest.mock import create_autospec
from django.db import models



# Create your models here.

class Crop(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Land(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class ConstructionBuilding(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class ProjectAffectedPerson(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    age = models.PositiveIntegerField()
    National_id_no = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    address = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    phone_number = models.PositiveIntegerField()
    crops = models.ForeignKey(Crop, on_delete=models.CASCADE)
    land = models.ForeignKey(Land, on_delete=models.CASCADE)
    construction = models.ForeignKey(ConstructionBuilding, on_delete=models.CASCADE)



    def __str__(self):
        return f"{self.first_name} {self.last_name}"


