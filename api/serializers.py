from unicodedata import category
from rest_framework import serializers
from .models import *

class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = ['name', 'description', 'quality', 'price', 'rating']

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['name', 'crops']

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
        'email','phone_number', 'type_of_crops', 'quantity_of_crops', 'construction_type','date']


