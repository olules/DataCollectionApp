from enum import auto
from random import choices
from unittest.mock import create_autospec
from unittest.util import _MAX_LENGTH
from django.db import models
from traitlets import default



# Create your models here.

class Crop(models.Model):
    QUALITY_CHOICES= (
        ('Mature_good', 'Mature_good'),
        ('Mature', 'Mature'),
        ('Immature_good', 'Immature_good'),
        ('Immature', 'Immature'),
    )
    name = models.CharField(max_length=60)
    description = models.TextField(max_length=256, blank=True, null=True)
    quality = models.CharField(max_length=13, choices = QUALITY_CHOICES)
    price = models.PositiveIntegerField(null=True, blank=True)
    rating = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=128)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE, related_name='crop_categories', null=True, blank=True)

    def __str__(self):
        return self.name

class Land(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=256, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class ConstructionBuilding(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=256, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Tree(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=256, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)

class ProjectAffectedPerson(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=128)
    id_no = models.CharField(max_length=100)
    email = models.EmailField(max_length=20)
    phone_number = models.PositiveIntegerField()
    trees = models.ForeignKey(Tree, on_delete=models.CASCADE, related_name='trees')
    type_of_crops = models.ForeignKey(Crop, on_delete=models.CASCADE, related_name='crops')
    quantity_of_crops = models.PositiveIntegerField()
    type_of_land = models.ForeignKey(Land, on_delete=models.CASCADE, related_name='land')
    construction_type = models.ForeignKey(ConstructionBuilding, on_delete=models.CASCADE, related_name='construction')
    date = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.User', related_name='pap', on_delete=models.CASCADE)



    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.address}"


