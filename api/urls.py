from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
    path('subcategories/', views.SubcategoryList.as_view()),
    path('subcategories/<int:pk>/', views.SubcategoryDetail.as_view()),
    path('crops/', views.CropList.as_view()),
    path('crops/<int:pk>/', views.CropDetail.as_view()),
    path('land/', views.LandList.as_view()),
    path('land/<int:pk>/', views.LandDetail.as_view()),
    path('building/', views.ConstructionBuildingList.as_view()),
    path('building/<int:pk>/', views.ConstructionBuildingDetail.as_view()),
     path('trees/', views.TreeList.as_view()),
    path('trees/<int:pk>/', views.TreeDetail.as_view()),
    path('pap/', views.ProjectAffectedPersonList.as_view()),
    path('pap/<int:pk>/', views.ProjectAffectedPersonDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)