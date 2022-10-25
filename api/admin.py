from django.contrib import admin
from .models import Category,Crop, PAPLand, Subcategory, Land, Tree, ProjectAffectedPerson, ConstructionBuilding


#Register your models here.
admin.site.register(Category)
admin.site.register(Crop)
admin.site.register(Subcategory)
admin.site.register(Land)
admin.site.register(Tree)
admin.site.register(ProjectAffectedPerson)
admin.site.register(PAPLand)
admin.site.register(ConstructionBuilding)
