from django.contrib import admin
from .models import Crop, Subcategory, Land, ProjectAffectedPerson, ConstructionBuilding


#Register your models here.
admin.site.register(Crop)
admin.site.register(Subcategory)
admin.site.register(Land)
admin.site.register(ProjectAffectedPerson)
admin.site.register(ConstructionBuilding)
