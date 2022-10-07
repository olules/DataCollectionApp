from unicodedata import category
from rest_framework import serializers
from .models import *

class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = ['name']

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['name']

class LandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Land
        fields = ['name']

class ConstructionBuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConstructionBuilding
        fields = ['name']

class ProjectAffectedPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectAffectedPerson
        fields = ['first_name', 'last_name', 'age', 'National_id_no', 'email', 
        'address', 'location', 'phone_number', 'crops', 'land', 'construction']


