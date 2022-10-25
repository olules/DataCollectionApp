from django.shortcuts import render
from api.models import *
from api.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, renderers
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import authentication, permissions
from django.contrib.auth.models import User


@api_view(['GET'])
def api_root(request, format = None):
   return Response({
      'land': reverse('land-list', request = request, format = format),
      'construction': reverse('construction-list', request = request, format = format),
      'trees': reverse('tree-list', request = request, format = format),
      'paps': reverse('pap-list', request = request, format = format),
      'crops': reverse('crop-list', request = request, format = format)
   })


# Create your views here.
# Category
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = SubcategorySerializer

#Subcategory
class SubcategoryList(APIView):
    """
    List all subcategories, or create a subcategory.
    """
    def get(self, request, format=None):
        subcategory = Subcategory.objects.all()
        serializer = SubcategorySerializer(subcategory, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SubcategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubcategoryDetail(APIView):
    """
    Retrieve, update or delete a subcategory instance.
    """
    def get_object(self, pk):
        try:
            return Subcategory.objects.get(pk=pk)
        except Subcategory.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        subcategory = self.get_object(pk)
        serializer = SubcategorySerializer(subcategory)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        subcategory = self.get_object(pk)
        serializer = SubcategorySerializer(subcategory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        subcategory = self.get_object(pk)
        subcategory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#Construction
class ConstructionBuildingList(generics.ListCreateAPIView):
    queryset = ConstructionBuilding.objects.all().order_by('name')
    serializer_class = ConstructionBuildingSerializer


class ConstructionBuildingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConstructionBuilding.objects.all().order_by('name')
    serializer_class = ConstructionBuildingSerializer

#Construction
class TreeList(generics.ListCreateAPIView):
    queryset = Tree.objects.all().order_by('name')
    serializer_class = TreeSerializer


class TreeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tree.objects.all().order_by('name')
    serializer_class = TreeSerializer


# Create your views here.
# Crop
class CropList(generics.ListCreateAPIView):
    queryset = Crop.objects.all().order_by('rating')
    serializer_class = CropSerializer

    def get_queryset(self):
        """
        This view should return a list of all the crops
        for the currently authenticated user.
        """
        user = self.request.user
        return Crop.objects.filter(owner=user).order_by('rating')



class CropDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Crop.objects.all().order_by('rating')
    serializer_class = CropSerializer

    def get_queryset(self):
        """
        This view should return a list of all the crop details
        for the currently authenticated user.
        """
        user = self.request.user
        return Crop.objects.filter(owner=user).order_by('rating')


#pap_crops
# ViewSets define the view behavior.
class PapCrop(APIView):
    """
    View to list all crops belonging to a pap in the system.
    """
    try:
        def get(self, request,first_name,format=None):
            pap = ProjectAffectedPerson.objects.get(first_name=first_name)
            pap_crops = Crop.objects.filter(pap=pap)
            serializer = CropSerializer(pap_crops, many=True)
            return Response(serializer.data)
    except Crop.DoesNotExist:
            raise Http404
    
    def get_queryset(self):
        """
        This view should return a list of all the paps
        for the currently authenticated user.
        """
        user = self.request.user
        return ProjectAffectedPerson.objects.filter(owner=user).order_by('-created')

#Land
class LandList(generics.ListCreateAPIView):
    queryset = Land.objects.all().order_by('name')
    serializer_class = LandSerializer


class LandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Land.objects.all().order_by('name')
    serializer_class = LandSerializer

            
#projected affected person
class ProjectAffectedPersonList(generics.ListCreateAPIView):
    queryset = ProjectAffectedPerson.objects.all().order_by('-created')
    serializer_class = ProjectAffectedPersonSerializer

    def get_queryset(self):
        """
        This view should return a list of all the project_affected_persons
        for the currently authenticated user.
        """
        user = self.request.user
        return ProjectAffectedPerson.objects.filter(owner=user).order_by('-created')


class ProjectAffectedPersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectAffectedPerson.objects.all().order_by('-created')
    serializer_class = ProjectAffectedPersonSerializer

    def get_queryset(self):
        """
        This view should return a list of all the project_affected_person_details
        for the currently authenticated user.
        """
        user = self.request.user
        return ProjectAffectedPerson.objects.filter(owner=user).order_by('-created')

#Project Affected Person's land
class PAPLandList(generics.ListCreateAPIView):
    queryset = PAPLand.objects.all().order_by('-created')
    serializer_class = PAPLandSerializer

    def get_queryset(self):
        """
        This view should return a list of all the project_affected_person land
        for the currently authenticated user.
        """
        user = self.request.user
        return PAPLand.objects.filter(owner=user).order_by('-created')


class PAPLandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PAPLand.objects.all().order_by('-created')
    serializer_class = PAPLandSerializer

    def get_queryset(self):
        """
        This view should return a list of all the project_affected_person land details
        for the currently authenticated user.
        """
        user = self.request.user
        return PAPLand.objects.filter(owner=user).order_by('-created')




