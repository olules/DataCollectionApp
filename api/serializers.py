from unicodedata import category
from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['category', 'name', 'slug']

class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = ['name', 'description', 'quality', 'price', 'rating']


class LandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Land
        fields = ['name', 'description', 'price']

class ConstructionBuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConstructionBuilding
        fields = ['name', 'description','price']

class TreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tree
        fields = ['name']

class ProjectAffectedPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectAffectedPerson
        fields = ['first_name', 'last_name', 'age', 'address', 'id_no', 
        'email','phone_number', 'trees','type_of_crops', 'quantity_of_crops', 'type_of_land','construction_type','created', 'updated']


