from django.shortcuts import render
from api.models import *
from api.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, renderers
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

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




# Create your views here.
# Crop
class CropList(APIView):
    """
    List all crops, or create a crop.
    """
    def get(self, request, format=None):
        crops = Crop.objects.all()
        serializer = CropSerializer(crops, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CropSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   

class CropDetail(APIView):
    """
    Retrieve, update or delete a crop instance.
    """
    def get_object(self, pk):
        try:
            return Crop.objects.get(pk=pk)
        except Crop.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        crop = self.get_object(pk)
        serializer = CropSerializer(crop)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        crop = self.get_object(pk)
        serializer = CropSerializer(crop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        crop = self.get_object(pk)
        crop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#projected affected person
class ProjectAffectedPersonList(generics.ListCreateAPIView):
    queryset = ProjectAffectedPerson.objects.all()
    serializer_class = ProjectAffectedPersonSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProjectAffectedPersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectAffectedPerson.objects.all()
    serializer_class = ProjectAffectedPersonSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
class ProjectAffectedPersonHighlight(generics.GenericAPIView):
    queryset = ProjectAffectedPerson.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        pap = self.get_object()
        return Response(pap.highlighted)




#Land
class LandList(generics.ListCreateAPIView):
    queryset = Land.objects.all()
    serializer_class = LandSerializer


class LandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Land.objects.all()
    serializer_class = LandSerializer

#Construction
class ConstructionBuildingList(generics.ListCreateAPIView):
    queryset = ConstructionBuilding.objects.all()
    serializer_class = ConstructionBuildingSerializer


class ConstructionBuildingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConstructionBuilding.objects.all()
    serializer_class = ConstructionBuildingSerializer

#Construction
class TreeList(generics.ListCreateAPIView):
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer


class TreeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer


