from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('', views.api_root),
    path('api/categories/', views.CategoryList.as_view()),
    path('api/categories/<int:pk>/', views.CategoryDetail.as_view()),
    path('api/subcategories/', views.SubcategoryList.as_view()),
    path('api/subcategories/<int:pk>/', views.SubcategoryDetail.as_view()),
    path('api/crops/', views.CropList.as_view(), name='crop-list'),
    path('api/crops/<int:pk>/', views.CropDetail.as_view(), name='crop-detail'),
    path('api/land/', views.LandList.as_view(), name='land-list'),
    path('api/land/<int:pk>/', views.LandDetail.as_view(), name='land-detail'),
    path('api/building/', views.ConstructionBuildingList.as_view(), name='construction-list'),
    path('api/building/<int:pk>/', views.ConstructionBuildingDetail.as_view(), name='construction-detail'),
    path('api/trees/', views.TreeList.as_view(), name='tree-list'),
    path('api/trees/<int:pk>/', views.TreeDetail.as_view(), name='tree-detail'),
    path('api/pap/', views.ProjectAffectedPersonList.as_view(), name='pap-list'),
    path('api/pap/<int:pk>/', views.ProjectAffectedPersonDetail.as_view(), name='pap-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)