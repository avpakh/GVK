# -*- coding: utf-8 -*-

import django_tables2 as tables
from .models import ReportTableLand
from .models import FindWO
from .models import Table1Use
from .models import Table2Obosob
from .models import Table3Arenda

from django_tables2.utils import A

class Table1(tables.Table):   # Main table

    inv_name = tables.LinkColumn('object_detail', args=[A('inv_num')])
    inv_name.verbose_name = "Название водного объекта"
    inv_num=tables.Column()
    inv_num.verbose_name = "Инвентарный номер водного объекта"
    inv_num.visible= False
    id=tables.Column()
    id.visible=False
    catwo=tables.Column()
    catwo.verbose_name = "Категория водного объекта"
    arraytype=tables.Column()
    arraytype.verbose_name = "Цель пользования "
    amount=tables.Column()
    amount.verbose_name = "Кол-во водных объектов"
    descr_location=tables.Column()
    descr_location.verbose_name="Привязка водных объектов"
    idcatwo=tables.Column()
    idcatwo.visible=False
    arendatype = tables.Column()
    arendatype.visible = False

    class Meta:
        model = ReportTableLand
        attrs= {"class":"paleblue"}
        fields = ('inv_name','catwo','arraytype','amount','descr_location')
        per_page = 15

class Table2(tables.Table): # Table with data from obosoble watersuse

    inv_name = tables.LinkColumn('object_detail', args=[A('inv_num')])
    inv_name.verbose_name = "Название водного объекта"
    inv_num=tables.Column()
    inv_num.verbose_name = "Инвентарный номер водного объекта"
    inv_num.visible= False
    id=tables.Column()
    id.visible=False
    catwo=tables.Column()
    catwo.verbose_name = "Категория водного объекта"
    obosobtype=tables.Column()
    obosobtype.verbose_name = "Цель обособленного пользования "
    amount=tables.Column()
    amount.verbose_name = "Кол-во водных объектов"
    descr_location=tables.Column()
    descr_location.verbose_name="Привязка водных объектов"
    idcatwo=tables.Column()
    idcatwo.visible=False

    class Meta:
        model = ReportTableLand
        attrs= {"class":"paleblue"}
        fields = ('inv_name', 'catwo', 'obosobtype', 'amount', 'descr_location')
        per_page = 15


class Table3(tables.Table): # Table with data from obosoble watersuse

    inv_name = tables.LinkColumn('object_detail', args=[A('inv_num')])
    inv_name.verbose_name = "Название водного объекта"
    inv_num=tables.Column()
    inv_num.verbose_name = "Инвентарный номер водного объекта"
    inv_num.visible= False
    id=tables.Column()
    id.visible=False
    catwo=tables.Column()
    catwo.verbose_name = "Категория водного объекта"
    areandatype=tables.Column()
    areandatype.verbose_name = "Цель передачи в аренду"
    amount=tables.Column()
    amount.verbose_name = "Кол-во водных объектов"
    descr_location=tables.Column()
    descr_location.verbose_name="Привязка водных объектов"
    idcatwo=tables.Column()
    idcatwo.visible=False

    class Meta:
        model = ReportTableLand
        attrs= {"class":"paleblue"}
        fields = ('inv_name', 'catwo', 'areandatype', 'amount', 'descr_location')
        per_page = 15

class Table4(tables.Table): # Table with data from obosoble watersuse

    inv_name = tables.LinkColumn('object_detail', args=[A('inv_num')])
    inv_name.verbose_name = "Название водного объекта"
    inv_num=tables.Column()
    inv_num.verbose_name = "Инвентарный номер водного объекта"
    inv_num.visible= False
    id=tables.Column()
    id.visible=False
    catwo=tables.Column()
    catwo.verbose_name = "Категория водного объекта"
    amount=tables.Column()
    amount.verbose_name = "Кол-во водных объектов"
    descr_location=tables.Column()
    descr_location.verbose_name="Привязка водных объектов"
    idcatwo=tables.Column()
    idcatwo.visible=False

    class Meta:
        model = ReportTableLand
        attrs= {"class":"paleblue"}
        fields = ('inv_name', 'catwo', 'arendatype', 'amount', 'descr_location')
        per_page = 15

class Table5(tables.Table): # Table with data from obosoble watersuse

    inv_name = tables.LinkColumn('object_find', args=[A('inv_num')])
    inv_name.verbose_name = "Название водного объекта"
    inv_num=tables.Column()
    inv_num.verbose_name = "Инвентарный номер водного объекта"
    inv_num.visible= False
    id=tables.Column()
    id.visible=False
    catwo=tables.Column()
    catwo.verbose_name = "Категория водного объекта"
    amount=tables.Column()
    amount.verbose_name = "Кол-во водных объектов"
    amount.visible= False
    descr_location=tables.Column()
    descr_location.verbose_name="Привязка водных объектов"
    idcatwo=tables.Column()
    idcatwo.visible=False
    sub_land = tables.Column()
    sub_land.verbose_name = " Наименование субъекта хозяйствования, в ведении которого находятся земли под водными объектами"
    sub_obosob = tables.Column()
    sub_obosob.verbose_name = "Наименование водопользователя, в обособленном водопользовании которого находится водный объект(ы) "
    sub_arenda = tables.Column()
    sub_arenda.verbose_name = "Наименование водопользователя, в аренду которому предоставлен водный объект"

    class Meta:
        model = FindWO
        attrs= {"class":"paleblue"}
        fields = ('inv_name', 'catwo', 'descr_location','sub_land','sub_obosob','sub_arenda')
        per_page = 15

class Table_use(tables.Table): # Table with data from obosoble watersuse
    id_tableuse= tables.Column()
    id_tableuse.visible=False
    inv_num=tables.Column()
    inv_num.verbose_name = "Инвентарный номер водного объекта"
    inv_num.visible= False
    land_naim = tables.Column()
    land_naim.verbose_name = "Наименование распорядительного органа"
    land_date=tables.Column()
    land_date.verbose_name = "Дата решения"
    land_desc=tables.Column()
    land_desc.verbose_name = "Номер решения"
    subject=tables.Column()
    subject.verbose_name = "наименование субъекта хозяйствования, в ведении которого находятся данные земли, целевое использование"
    addition=tables.Column()
    addition.verbose_name = "Дополнительная информация"
    watprot = tables.Column()
    watprot.verbose_name = "Информация по водоохранным зонам"

    class Meta:
        model = Table1Use
        attrs = {"class": "paleblue"}
        fields = ('land_naim', 'land_date', 'land_desc', 'subject', 'addition','watprot')
        per_page = 15
        orderable = False

class Table_obosob(tables.Table): # Table with data from obosoble watersuse
    id_tableobosob= tables.Column()
    id_tableobosob.visible=False
    inv_num=tables.Column()
    inv_num.verbose_name = "Инвентарный номер водного объекта"
    inv_num.visible= False
    name_d = tables.Column()
    name_d.verbose_name = "Наименование распорядительного органа"
    data_d=tables.Column()
    data_d.verbose_name = "Дата решения"
    num_r=tables.Column()
    num_r.verbose_name = "Номер решения"
    wateruser=tables.Column()
    wateruser.verbose_name = "Наименование водопользователя, в обособленном водопользовании которого находится водный объект"
    w_len = tables.Column()
    w_len.verbose_name = "Протяженность участка водотока, км"
    area = tables.Column()
    area.verbose_name = " Площадь поверхности воды водоема, га"
    targetobosobwu = tables.Column()
    targetobosobwu.verbose_name = "Цель обособленного водопользования"
    data_exp = tables.Column()
    data_exp.verbose_name = "дата окончания права обособленного водопользования "
    document = tables.Column()
    document.verbose_name = " Документ, удостоверяющий право обособленного водопользования, и его реквизиты * "

    class Meta:
        model = Table2Obosob
        attrs = {"class": "paleblue"}
        fields = ('name_d', 'data_d', 'num_r', 'wateruser', 'w_len','area','targetobosobwu','data_exp','document')
        per_page = 15
        orderable = False

class Table_arenda(tables.Table): # Table with data from obosoble watersuse
    id_tableobosob= tables.Column()
    id_tableobosob.visible=False
    inv_num=tables.Column()
    inv_num.verbose_name = "Инвентарный номер водного объекта"
    inv_num.visible= False
    reasons = tables.Column()
    reasons.verbose_name = "Основание заключения договора аренды"
    target_ar=tables.Column()
    target_ar.verbose_name = "Цель передачи в аренду"
    wateruser=tables.Column()
    wateruser.verbose_name = "Наименование водопользователя, в аренду которому предоставлен водный объект"
    part_len = tables.Column()
    part_len.verbose_name = "Протяженность участка водотока, км"
    part_area = tables.Column()
    part_area = " Площадь поверхности воды водоема, га"
    end_date = tables.Column()
    end_date.verbose_name = "Дата окончания договора аренды "

    class Meta:
        model = Table3Arenda
        attrs = {"class": "paleblue"}
        fields = ('reasons', 'target_ar', 'wateruser', 'part_len','part_area','end_date')
        per_page = 15
        orderable = False

