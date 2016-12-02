# -*- coding: utf-8 -*-

import django_filters
from .models import ReportTableLand
from .models import FindWO
from django_filters.filters import CharFilter



EMPTY_CHOICE = ('', '---------'), # Don't forget the trailing comma


class ReportTableLandFilter(django_filters.FilterSet):

    descr_location = django_filters.CharFilter(label='Территориальная привязка (область, район, населенный пункт) (ввод в строке)',lookup_type='contains')
    inv_name = django_filters.CharFilter(label='Название водного объекта (ввод в строке)', lookup_type='contains')


    class Meta:
        model = ReportTableLand
        fields = ['catwo','descr_location','inv_name']
        order_by = (('catwo',u'Категория водных объектов'),)


    def __init__(self, *args, **kwargs):
        super(ReportTableLandFilter, self).__init__(*args, **kwargs)
        self.filters['catwo'].extra['choices'] = EMPTY_CHOICE + \
           self.filters['catwo'].extra['choices']


class ReportTableFindFilter(django_filters.FilterSet):

    descr_location = django_filters.CharFilter(label='Территориальная привязка (область, район, населенный пункт) (ввод в строке)',lookup_type='contains')
    inv_name = django_filters.CharFilter(label='Название водного объекта (ввод в строке)', lookup_type='contains')
    sub_land = django_filters.CharFilter(label='Наименование субъекта хозяйствования, в ведении которого находятся земли под водными объектами (ввод в строке)', lookup_type='contains')
    sub_obosob = django_filters.CharFilter(label='Наименование водопользователя, в обособленном водопользовании которого находится водный объект(ы) (ввод в строке)', lookup_type='contains')
    sub_arenda = django_filters.CharFilter(label='Наименование водопользователя, в аренду которому предоставлен водный объект (ввод в строке)', lookup_type='contains')

    class Meta:
        model = FindWO
        fields = ['catwo','descr_location','inv_name','sub_land','sub_obosob','sub_arenda']
        order_by = (('catwo',u'Категория водных объектов'),)


    def __init__(self, *args, **kwargs):
        super(ReportTableFindFilter, self).__init__(*args, **kwargs)
        self.filters['catwo'].extra['choices'] = EMPTY_CHOICE + \
           self.filters['catwo'].extra['choices']
