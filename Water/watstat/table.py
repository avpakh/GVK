# -*- coding: utf-8 -*-

import django_tables2 as tables
from .models import ReportBasinData
from django_tables2_reports.tables import TableReport




from django_tables2.utils import A


class ReportBasin(tables.Table):   # Main table

    nai=tables.Column()
    nai.verbose_name = "Название речного бассейна"
    god=tables.Column()
    god.verbose_name = "Год"
    x1=tables.Column()
    x1.verbose_name = "x1"
    x2=tables.Column()
    x2.verbose_name = "x2"
    x3=tables.Column()
    x3.verbose_name = "x3"
    x4=tables.Column()
    x4.verbose_name = "x4"
    x5=tables.Column()
    x5.verbose_name = "x5"
    x6=tables.Column()
    x6.verbose_name = "x6"
    x7=tables.Column()
    x7.verbose_name = "x7"
    x8=tables.Column()
    x8.verbose_name = "x8"
    x9 = tables.Column()
    x9.verbose_name = "x9"
    x10 = tables.Column()
    x10.verbose_name = "x10"
    x11 = tables.Column()
    x11.verbose_name = "x11"
    x12 = tables.Column()
    x12.verbose_name = "x12"
    x13 = tables.Column()
    x13.verbose_name = "x13"


    class Meta:
        model = ReportBasinData
        attrs= {"class":"paleblue"}
        fields = ('nai','god','x1','x2','x3','x4','x5','x6','x7','x8')
        per_page = 15


class ReportBasinNewTable(TableReport):   # Main table

    nai=tables.Column()
    nai.verbose_name = "Название речного бассейна"
    param=tables.Column()
    param.verbose_name = "Название параметра"
    x1=tables.Column()
    x1.verbose_name = "2000"
    x2=tables.Column()
    x2.verbose_name = "2001"
    x3=tables.Column()
    x3.verbose_name = "2002"
    x4=tables.Column()
    x4.verbose_name = "2003"
    x5=tables.Column()
    x5.verbose_name = "2004"
    x6=tables.Column()
    x6.verbose_name = "2005"
    x7=tables.Column()
    x7.verbose_name = "2006"
    x8=tables.Column()
    x8.verbose_name = "2007"
    x9 = tables.Column()
    x9.verbose_name = "2008"
    x10 = tables.Column()
    x10.verbose_name = "2009"
    x11 = tables.Column()
    x11.verbose_name = "2010"
    x12 = tables.Column()
    x12.verbose_name = "2011"
    x13 = tables.Column()
    x13.verbose_name = "2012"
    x14 = tables.Column()
    x14.verbose_name = "2013"
    x15 = tables.Column()
    x15.verbose_name = "2014"
    x16 = tables.Column()
    x16.verbose_name = "2015"

    class Meta:
        model = ReportBasinData
        attrs= {"class":"paleblue", "width":"80%"}
        fields = ('nai','param','x1','x2','x3','x4','x5','x6','x7','x8','x9','x10','x11','x12','x13','x14','x15','x16')
        per_page = 15
