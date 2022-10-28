from django.shortcuts import render
from api.models import *
from api.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, renderers, filters
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
import django_filters.rest_framework
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

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
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Category.objects.all()
    serializer_class = SubcategorySerializer

#Subcategory
class SubcategoryList(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

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
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

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
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = ConstructionBuilding.objects.all().order_by('name')
    serializer_class = ConstructionBuildingSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']



class ConstructionBuildingDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = ConstructionBuilding.objects.all().order_by('name')
    serializer_class = ConstructionBuildingSerializer

#Construction
class TreeList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Tree.objects.all().order_by('name')
    serializer_class = TreeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']



class TreeDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Tree.objects.all().order_by('name')
    serializer_class = TreeSerializer


# Create your views here.
# Crop
class CropList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Crop.objects.all().order_by('rating')
    serializer_class = CropSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    
    def create(self, request, *args, **kwargs):
        owner = request.user
        data = {
            "pap": request.POST.get('pap', None),
            "owner": owner.id,
            }
        _serializer = self.serializer_class(data=data)  # NOQA
        if _serializer.is_valid():
            _serializer.save()
            return Response(data=_serializer.data, status=status.HTTP_201_CREATED)  # NOQA
        else:
            return Response(data=_serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # NOQA
    
    def get_queryset(self):
        """
        This view should return a list of all the crop details
        for the currently authenticated user.
        """
        user = self.request.user
        return Crop.objects.filter(owner=user).order_by('rating')
    
    

    
class CropDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Crop.objects.all().order_by('rating')
    serializer_class = CropSerializer

    def get_queryset(self):
        """
        This view should return a list of all the crop details
        for the currently authenticated user.
        """
        user = self.request.user
        return Crop.objects.filter(owner=user).order_by('rating')



#Land
class LandList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Land.objects.all().order_by('name')
    serializer_class = LandSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']



class LandDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Land.objects.all().order_by('name')
    serializer_class = LandSerializer

            
#projected affected person
class ProjectAffectedPersonList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = ProjectAffectedPerson.objects.all().order_by('-created')
    serializer_class = ProjectAffectedPersonSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'id_no']


    def get_queryset(self):
        """
        This view should return a list of all the project_affected_persons
        for the currently authenticated user.
        """
        user = self.request.user
        return ProjectAffectedPerson.objects.filter(owner=user).order_by('-created')

    
    

class ProjectAffectedPersonDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = ProjectAffectedPerson.objects.all().order_by('-created')
    serializer_class = ProjectAffectedPersonSerializer

    def get_queryset(self):
        """
        This view should return a list of all the project_affected_person_details
        for the currently authenticated user.
        """
        user = self.request.user
        return ProjectAffectedPerson.objects.filter(owner=user).order_by('-created')

#pap_crops
# ViewSets define the view behavior.
class PapCrop(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
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
    

#Project Affected Person's land
class PAPLandList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = PAPLand.objects.all().order_by('-created')
    serializer_class = PAPLandSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    def get_queryset(self):
        """
        This view should return a list of all the project_affected_person land
        for the currently authenticated user.
        """
        user = self.request.user
        return PAPLand.objects.filter(owner=user).order_by('-created')


class PAPLandDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = PAPLand.objects.all().order_by('-created')
    serializer_class = PAPLandSerializer

    def get_queryset(self):
        """
        This view should return a list of all the project_affected_person land details
        for the currently authenticated user.
        """
        user = self.request.user
        return PAPLand.objects.filter(owner=user).order_by('-created')

#pap_land
# ViewSets define the view behavior.
class PapLandView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    """
    View to list all land belonging to a particular pap.
    """
    try:
        def get(self, request,first_name,format=None):
            pap = ProjectAffectedPerson.objects.get(first_name=first_name)
            pap_land = PAPLand.objects.filter(pap=pap)
            serializer = PAPLandSerializer(pap_land, many=True)
            return Response(serializer.data)
    except PAPLand.DoesNotExist:
            raise Http404
    
    def get_queryset(self):
        """
        This view should return a list of all the paps
        for the currently authenticated user.
        """
        user = self.request.user
        return ProjectAffectedPerson.objects.filter(owner=user).order_by('-created')





