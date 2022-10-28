from enum import auto
from random import choices
from unittest.mock import create_autospec
from unittest.util import _MAX_LENGTH
from django.db import models
from traitlets import default



# Create your models here.
# Class model for category
class Category(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


# Class model for subcategory
class Subcategory(models.Model):
    category = models.ForeignKey(Category,related_name='category',on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200,db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'

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

    def __str__(self):
        return self.name

class Land(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=256, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'land'
        verbose_name_plural = 'land'

    def __str__(self):
        return self.name

class ProjectAffectedPerson(models.Model):
    CROPS= (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=128)
    id_no = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=20, unique=True)
    phone_number = models.PositiveIntegerField()
    trees = models.ForeignKey(Tree, on_delete=models.CASCADE, related_name='trees')
    crops = models.CharField(max_length=13, choices = CROPS)
    type_of_land = models.ForeignKey(Land, on_delete=models.CASCADE, related_name='lands')
    construction_type = models.ForeignKey(ConstructionBuilding, on_delete=models.CASCADE, related_name='construction')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.User', related_name='owners', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} { self.last_name} { self.address}"



# Class model for crop
class Crop(models.Model):
    QUALITY_CHOICES= (
        ('Mature_good', 'Mature_good'),
        ('Mature', 'Mature'),
        ('Immature_good', 'Immature_good'),
        ('Immature', 'Immature'),
    )
    subcategory = models.ForeignKey(Subcategory,related_name='subcategories',on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    description = models.TextField(max_length=256, blank=True, null=True)
    quantity = models.PositiveIntegerField()
    quality = models.CharField(max_length=13, choices = QUALITY_CHOICES)
    price = models.PositiveIntegerField(null=True, blank=True)
    rating = models.PositiveIntegerField(null=True, blank=True)
    pap = models.ForeignKey(ProjectAffectedPerson, related_name='pap_crops',on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='users', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.pap} {self.quantity}"


class PAPLand(models.Model):
    TENURE_TYPES= (
        ('Mailo Land', 'Mailo Land'),
        ('Freehold Land', 'Freehold Land'),
        ('Lease Land', 'Lease Land'),
        ('Customary Land', 'Customer Land')
    )
    type_of_land = models.ForeignKey(Land, on_delete=models.CASCADE, related_name='pap_land')
    survey_no = models.CharField(max_length=200, blank=True, null=True)
    pap = models.ForeignKey(ProjectAffectedPerson, related_name='land_owners', on_delete=models.CASCADE)
    tenure = models.CharField(max_length=20, choices = TENURE_TYPES)
    size = models.PositiveBigIntegerField()
    location = models.CharField(max_length=255)
    land_use = models.TextField(blank=True, null=True)
    land_services  = models.TextField(blank=True, null=True)
    rate = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.User', related_name='paplands', on_delete=models.CASCADE)




    
