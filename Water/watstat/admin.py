from django.contrib import admin
from .widgets import MPTTModelMultipleChoiceField
from .widgets import MPTTFilteredSelectMultiple
from .models import ProductCategory
from .models import Parameters
from .models import  Adm_level
from .models import Economy_level
from .models import Group

from django import forms


# Register your models here.

class ProductForm(forms.ModelForm):
    categories = MPTTModelMultipleChoiceField(
                    ProductCategory.objects.all(),
                    widget = MPTTFilteredSelectMultiple("Categories",False,attrs={'rows':'10'})
                )
    class Meta:
        model= ProductCategory
        fields = "__all__"

class ProductAdmin(admin.ModelAdmin):
    form = ProductForm

class ParametersAdmin(admin.ModelAdmin):

    search_fields = ['name']
    list_display =  ['name','group']
    list_filter = ['name','group']

    class Meta:
        model = Parameters
    pass

class GroupAdmin(admin.ModelAdmin):

    search_fields = ['group_name']
    list_display =  ['group_name']
    list_filter = ['group_name']

    class Meta:
        model = Group
    pass

class CategoriesAdmin(admin.ModelAdmin):

    class Meta:
        model = ProductCategory
    pass

class Adm_levelAdmin(admin.ModelAdmin):

    search_fields = ['name']
    list_display = ['name','code']
    list_filter = ['name']

    class Meta:
        model = Adm_level
    pass

class Economy_levelAdmin(admin.ModelAdmin):

    search_fields = ['nai']
    list_display = ['nai','kod0','kod1']
    list_filter = ['nai']

    class Meta:
        model = Economy_level
    pass

admin.site.register(ProductCategory,ProductAdmin)
admin.site.register(Group,GroupAdmin)
admin.site.register(Parameters,ParametersAdmin)
admin.site.register(Adm_level,Adm_levelAdmin)
admin.site.register(Economy_level,Economy_levelAdmin)