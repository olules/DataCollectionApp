from attr import fields
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import *
from rest_framework import permissions

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['category', 'name', 'slug']

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
    trees = serializers.SlugRelatedField(
        queryset = Tree.objects.all(),
        slug_field='name',
    )

    type_of_land = serializers.SlugRelatedField(
        queryset = Land.objects.all(),
        slug_field='name'
    )

    construction_type = serializers.SlugRelatedField(
        queryset = ConstructionBuilding.objects.all(),
        slug_field='name'
    )
    
    class Meta:
        model = ProjectAffectedPerson
        fields = ['first_name', 'last_name', 'age', 'address', 'id_no', 'email','phone_number', 
        'trees','crops', 'type_of_land','construction_type','created', 'updated','owner']

    
class CropSerializer(serializers.ModelSerializer):
    pap = serializers.SlugRelatedField(
        queryset = ProjectAffectedPerson.objects.all(),
        slug_field='first_name'
    )
    
    class Meta:
        model = Crop
        fields = ['name', 'description', 'quantity','quality', 'price', 'rating', 'pap']

class PAPLandSerializer(serializers.ModelSerializer):
    type_of_land = serializers.SlugRelatedField(
        queryset = Land.objects.all(),
        slug_field='name'
    )
    pap_land = serializers.SlugRelatedField(
        queryset = ProjectAffectedPerson.objects.all(),
        slug_field='first_name'
    )
    class Meta:
        model = PAPLand
        fields = ['type_of_land', 'survey_no', 'pap_name','tenure', 'size', 'location', 'land_use', 
                    'land_services', 'rate', 'created', 'updated']

    




