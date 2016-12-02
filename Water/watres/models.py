# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.postgres.fields import ArrayField
from django.contrib.gis.db import models as models



# Create your models here.


SELECT_CATWO = (
    ('родник', 'родник'),
    ('пруд', 'пруд'),
    ('пруд-копань', 'пруд-копань'),
    ('обводненный карьер', 'обводненный карьер'),
    ('озеро (естественный водоем)','озеро (естественный водоем)'),
    ('водохранилище','водохранилище'),
    ('канал','канал'),
    ('ручей', 'ручей'),
    ('река, малая','река, малая'),
    ('река, средняя', 'река, средняя'),
    ('река, большая', 'река, большая'),
)

class TypeWO (models.Model):
    id_typewo = models.AutoField(primary_key=True)
    typewo_name=models.CharField('Тип водного объекта (линейный/площадной/точечный)', max_length=50)

    class Meta:
        verbose_name = 'Тип водного объекта'
        verbose_name_plural = 'Типы водных объектов'

    def __unicode__(self):
        return u" %s " % (self.typewo_name)


class Gvk (models.Model):
    id_gvk = models.AutoField(primary_key=True)
    gup = models.IntegerField('Код ГВК')
    oku = models.CharField('УНП', max_length=9,blank=True)
    ato = models.CharField('ATO', max_length=10,blank=True)
    npr = models.CharField('Название предприятия',max_length=500,blank=True)
    okpo = models.CharField('ОКПО', max_length=12,blank=True)
    correctlink= models.BooleanField('Correct',blank=True)
    newokpo=models.CharField('ОКПО верифицированный', max_length=12,blank=True)
    npr_zat=models.CharField('Название предприятия',max_length=500,blank=True)

class Zat (models.Model):
    id_zat = models.AutoField(primary_key=True)
    kod = models.CharField('Код ОКПО',max_length=12)
    okulp = models.CharField('УНП', max_length=9)
    ato = models.CharField('OКЕ', max_length=10)
    npr = models.CharField('Название предприятия',max_length=500)

class CatWO (models.Model):
    id_catwo = models.AutoField(primary_key=True)
    catwo_name = models.CharField('Категория водного объекта', max_length=50)
    catwo_description = models.CharField('Описание категории водного объекта', max_length=200,blank=True)
    catwo_type_id = models.ForeignKey(TypeWO)

    class Meta:

        verbose_name = 'Категория водного объекта'
        verbose_name_plural = 'Категории водных объектов'

class SoatoData(models.Model):
    id_soato = models.AutoField(primary_key=True)
    soato_kode = models.CharField('Код СОATO',max_length=10)
    soato_name = models.CharField('Название',max_length=200)
    soato_nameadd = models.CharField('Название дополнительное', max_length=200)

    class Meta:
        db_table = u'SoatoData'

        verbose_name = 'Данные по коду СОAТО'
        verbose_name_plural = 'Данные по кодам СОАТО'

    def __unicode__(self):
        return u" %s  %s  %s " % (self.soato_nameadd,self.soato_name,self.soato_kode)


class PolygonWO(models.Model):
    name = models.CharField(max_length=100)
    poly = models.PolygonField(srid=4326) # we want our model in a different SRID
    idwo = models.CharField
    id_num = models.IntegerField()
    objects = models.GeoManager()

    @property
    def popupContent(self):
        return self.name


    def __unicode__(self):
        return u" %s " % (self.name)

testgeo_mappingp={
    'name': 'F09',
    'poly': 'POLYGON',}


class LineWO(models.Model):
    name = models.CharField(max_length=100) # corresponds to the 'str' field
    line = models.MultiLineStringField(srid=4326) # we want our model in a different SRID
    id_num = models.IntegerField()
    objects = models.GeoManager()

    @property
    def popupContent(self):
        return self.name

    def __unicode__(self):
        return u" %s %s" % (self.name,self.id_num)


class PointWO(models.Model):
    name = models.CharField(max_length=100) # corresponds to the 'str' field
    point = models.PointField(srid=4326) # we want our model in a different SRID
    id_num = models.IntegerField()
    objects = models.GeoManager()

    @property
    def popupContent(self):
        return self.name

    def __unicode__(self):
        return u" %s " % (self.name)


class ReportTableLand(models.Model):
    inv_name = models.CharField(max_length=200)
    inv_num = models.IntegerField()
    catwo = models.CharField('Название категории для водных объектов - выбор из списка',max_length=150,choices=SELECT_CATWO,default='')
    arraytype = models.CharField(max_length=250)
    amount = models.IntegerField()
    descr_location = models.CharField('Территориальная привязка',max_length=400)
    idcatwo = models.IntegerField()
    obosobtype = models.CharField(max_length=250)
    areandatype = models.CharField(max_length=250)

    def __unicode__(self):
        return u" %s %s " % (self.inv_name,self.catwo)


class FindWO(models.Model):
    inv_name = models.CharField(max_length=200)
    inv_num = models.IntegerField()
    catwo = models.CharField('Название категории для водных объектов - выбор из списка', max_length=150,
                             choices=SELECT_CATWO, default='')
    arraytype = models.CharField(max_length=250)
    amount = models.IntegerField()
    descr_location = models.CharField('Территориальная привязка', max_length=400)
    idcatwo = models.IntegerField()
    sub_land = models.CharField(max_length=550)
    sub_obosob = models.CharField(max_length=550)
    sub_arenda = models.CharField(max_length=550)
    obosobtype = models.CharField(max_length=550)
    areandatype = models.CharField(max_length=550)


    def __unicode__(self):
        return u" %s %s " % (self.inv_name, self.catwo)

class InvWatObjPoint(models.Model):
    inv_name = models.CharField(max_length=100)
    inv_num = models.IntegerField()
    id_catwo = models.IntegerField(blank=True)
    type_array = ArrayField(models.IntegerField(), null=True)
    amount = models.IntegerField()
    descr_location = models.CharField(max_length=400)
    soato = models.ForeignKey(SoatoData)
    mygeo = models.ForeignKey(PolygonWO)


    def __unicode__(self):
        return u" %s " % (self.inv_name)


class InvWatObjLine(models.Model):
    inv_name = models.CharField(max_length=300)
    inv_num = models.IntegerField()
    id_catwo = models.IntegerField(blank=True)
    type_array=ArrayField(models.IntegerField(),null=True)
    amount = models.IntegerField()
    raion = models.CharField(max_length=400)
    descr = models.CharField(max_length=400)
    mygeo = models.ForeignKey(LineWO)

    @property
    def popupContent(self):
        return self.inv_name

    def __unicode__(self):
        return u" %s " % (self.inv_name)


class InvWatObjPoly(models.Model):
    inv_name = models.CharField(max_length=100)
    inv_num = models.IntegerField()
    id_catwo = models.IntegerField(blank=True)
    type_array = ArrayField(models.IntegerField(), null=True)
    amount = models.IntegerField()
    descr_location = models.CharField(max_length=400)
    soato = models.ForeignKey(SoatoData)
    mygeo = models.ForeignKey(PolygonWO)

    @property
    def popupContent(self):
        return self.inv_name

    def __unicode__(self):
        return u" %s " % (self.inv_name)

class  Table1Use(models.Model):
    id_tableuse= models.AutoField(primary_key=True)
    inv_num = models.IntegerField()
    land_naim = models.CharField(max_length=300,blank=True,null=True)
    land_date = models.CharField(max_length=20,blank=True,null=True)
    land_desc = models.CharField(max_length=20,blank=True,null=True)
    subject = models.CharField(max_length=500,blank=True,null=True)
    subject_array = ArrayField(models.IntegerField(),null=True)
    target_use=models.CharField(max_length=200,blank=True,null=True)
    addition=models.CharField(max_length=800,blank=True,null=True)
    watprot=models.CharField(max_length=800,blank=True,null=True)

    def __unicode__(self):
        return u" %s " % (self.inv_num)

class  Table2Obosob(models.Model):
    id_tableobosob= models.AutoField(primary_key=True)
    inv_num = models.IntegerField()
    name_d = models.CharField(max_length=200,blank=True,null=True)
    data_d = models.CharField(max_length=200,blank=True,null=True)
    num_r = models.CharField(max_length=200, blank=True, null=True)
    wateruser = models.CharField(max_length=300,blank=True,null=True)
    id_targetwuse = ArrayField(models.IntegerField(), null=True)
    w_len = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    area = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    targetobosobwu = models.CharField(max_length=500,blank=True,null=True)
    data_expl = models.CharField(max_length=500,blank=True,null=True)
    document = models.CharField(max_length=500,blank=True,null=True)
    def __unicode__(self):
        return u" %s " % (self.inv_num)

class  Table3Arenda(models.Model):
    id_tablearenda= models.AutoField(primary_key=True)
    inv_num = models.IntegerField()
    reasons = models.CharField(max_length=200,blank=True,null=True)
    target_ar = models.CharField(max_length=200,blank=True,null=True)
    wateruser = models.CharField(max_length=300,blank=True,null=True)
    id_arenda = ArrayField(models.IntegerField(), null=True)
    part_len = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    part_area = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    end_date = models.CharField(max_length=20,blank=True,null=True)

class Table4Recreation(models.Model):
    id_tablerecreation = models.AutoField(primary_key=True)
    inv_num = models.IntegerField()
    location = models.CharField(max_length=300, blank=True, null=True)
    responsible_b = models.CharField(max_length=200, blank=True, null=True)
    decision_date = models.CharField( max_length=20, blank=True, null=True)
    decision_num = models.CharField(max_length=30, blank=True, null=True)

    def __unicode__(self):
        return u" %s " % (self.inv_num)


testgeo_mappingl={
    'name': 'NAME',
    'line': 'MULTILINESTRING',}

class TargetUseWO (models.Model):
    id_targetusewo = models.AutoField(primary_key=True)
    targetusewo_name=models.CharField('Цель пользования водными ресурсами', max_length=80)
    checkin=models.BooleanField()

    class Meta:
        verbose_name = 'Цель пользования водными объектами'
        verbose_name_plural = 'Цели пользования водными объектами'


    def __unicode__(self):
        return u" %s %s " % (self.id_targetusewo, self.targetusewo_name)

class TargetUseWOExBody (models.Model):
    id_targetusewoexbody = models.AutoField(primary_key=True)
    targetusewoexbody_name=models.CharField('Целевое использование', max_length=80,blank=True)

    class Meta:
        verbose_name = 'Целевое использование'
        verbose_name_plural = 'Целевое использование'


    def __unicode__(self):
        return u" %s " % (self.targetusewoexbody_name)

class TargetArendaWO (models.Model):
    id_targetarendawo = models.AutoField(primary_key=True)
    targetarendawo_name=models.CharField('Цель передачи в аренду', max_length=200,blank=True)
    checkin = models.BooleanField()

    class Meta:
        verbose_name = 'Цель передачи в аренду'
        verbose_name_plural = 'Цели передачи в аренду '


    def __unicode__(self):
        return u" %s " % (self.targetarendawo_name)


class TargetObosobWOuse (models.Model):
    id_targetobosobwouse = models.AutoField(primary_key=True)
    targetobosobwouse_name=models.CharField('Цель обособленного водопользования', max_length=200,blank=True)
    checkin = models.BooleanField()

    class Meta:
        verbose_name = 'Цель обособленного водопользования'
        verbose_name_plural = 'Цели обособленного водопользования'


    def __unicode__(self):
        return u" %s " % (self.targetobosobwouse_name)

class ExBodyData(models.Model):

    id_exbody=models.AutoField(primary_key=True)
    name_exbody=models.CharField("Наименование местного исполнительного и распорядительного органа",max_length=200)
    soato=models.ForeignKey(SoatoData)

    class Meta:
        verbose_name= 'Орган власти'
        verbose_name_plural = 'Органы власти'

