# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from .models import ExBodyData # Исполнительный орган

from .models import SoatoData # Данные СОАТО

from .models import CatWO  # Данные Категории статья №5 ВК РБ

from .models import TypeWO # Данные Типы водных объектов исходя из геометрии (точечный / линейный / площадной)

from .models import TargetUseWO # Цели водопользования статья №38 ВК РБ

from .models import TargetArendaWO # Цели пердачи водного объекта в аренду

from .models import TargetObosobWOuse # Цели обособленного водопользования

from .models import TargetUseWOExBody # Цели использования земель под водными объектами

from .models import PolygonWO

from .models import LineWO

from .models import PointWO

from .models import InvWatObjLine

from .models import InvWatObjPoly

from .models import InvWatObjPoint

from .models import ReportTableLand

from .models import FindWO


from leaflet.admin import LeafletGeoAdmin


class FindWOAdmin(admin.ModelAdmin):

    search_fields = ['inv_name']
    list_display =  ['inv_name']
    list_filter = ['inv_name']

    class Meta:
        model = FindWO
    pass


class ReportTableLandAdmin(admin.ModelAdmin):

    search_fields = ['inv_name']
    list_display =  ['inv_name']
    list_filter = ['inv_name']

    class Meta:
        model = ReportTableLand
    pass

class InvWatObjLineAdmin(admin.ModelAdmin):

    search_fields = ['inv_name']
    list_display =  ['inv_name']
    list_filter = ['inv_name']

    class Meta:
        model = InvWatObjLine
    pass


class InvWatObjPolyAdmin(admin.ModelAdmin):

    search_fields = ['inv_name']
    list_display =  ['inv_name']
    list_filter = ['inv_name']

    class Meta:
        model = InvWatObjPoly
    pass

class InvWatObjPointAdmin(admin.ModelAdmin):

    search_fields = ['inv_name']
    list_display =  ['inv_name']
    list_filter = ['inv_name']

    class Meta:
        model = InvWatObjPoint
    pass


class TargetArendaWOAdmin(admin.ModelAdmin):

    search_fields = ['targetarendawo_name']
    list_display =  ['targetarendawo_name']
    list_filter = ['targetarendawo_name']

    class Meta:
        model = TargetArendaWO
    pass



class TargetObosobWOuseAdmin(admin.ModelAdmin):

    search_fields = ['targetobosobwouse_name']
    list_display =  ['targetobosobwouse_name']
    list_filter = ['targetobosobwouse_name']

    class Meta:
        model = TargetObosobWOuse
    pass

class TargetUseWOExbodyAdmin(admin.ModelAdmin):

    search_fields = ['targetusewoexbody_name']
    list_display =  ['targetusewoexbody_name']
    list_filter = ['targetusewoexbody_name']

    class Meta:
        model = TargetUseWOExBody
    pass


class ExBodyAdmin(admin.ModelAdmin):

    search_fields = ['name_exbody']
    list_editable = ['name_exbody']
    list_display = ['name_exbody']
    list_display_links = None
    list_per_page = 10

    class Meta:
        model = ExBodyData

    def get_form(self, request, obj=None, **kwargs):
        form = super(ExBodyAdmin,self).get_form(request, obj, **kwargs)
        form.base_fields['soato'].queryset =SoatoData.objects.filter(soato_nameadd__contains='г ')
        return form


class SoatoAdmin(admin.ModelAdmin):

    search_fields = ['soato_nameadd']
    list_display =  ['soato_nameadd']
    list_filter = ['soato_nameadd']

    class Meta:
        model = SoatoData
    pass

class TargetUseWOAdmin(admin.ModelAdmin):

    search_fields = ['targetusewo_name']
    list_display =  ['targetusewo_name']
    list_filter = ['targetusewo_name']

    class Meta:
        model = TargetUseWO
    pass

class CatWOAdmin(admin.ModelAdmin):

    search_fields = ['catwo_name']
    list_display =  ['catwo_name']
    list_filter = ['catwo_name']

    class Meta:
        model = CatWO
    pass

class TypeWOAdmin(admin.ModelAdmin):

    search_fields = ['typewo_name']
    list_display =  ['typewo_name']
    list_filter = ['typewo_name']

    class Meta:
        model = TypeWO
    pass


admin.site.register(PolygonWO,LeafletGeoAdmin)
admin.site.register(PointWO,LeafletGeoAdmin)
admin.site.register(LineWO,LeafletGeoAdmin)

admin.site.register(FindWO,FindWOAdmin)
admin.site.register(ExBodyData,ExBodyAdmin)
admin.site.register(InvWatObjLine,InvWatObjLineAdmin)
admin.site.register(ReportTableLand,ReportTableLandAdmin)
admin.site.register(InvWatObjPoly,InvWatObjPolyAdmin)
admin.site.register(InvWatObjPoint,InvWatObjPointAdmin)
admin.site.register(SoatoData,SoatoAdmin)
admin.site.register(CatWO,CatWOAdmin)
admin.site.register(TypeWO,TypeWOAdmin)
admin.site.register(TargetUseWO,TargetUseWOAdmin)
admin.site.register(TargetObosobWOuse,TargetObosobWOuseAdmin)
admin.site.register(TargetArendaWO,TargetArendaWOAdmin)
admin.site.register(TargetUseWOExBody,TargetUseWOExbodyAdmin)

