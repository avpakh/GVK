# -*- coding: utf-8 -*-

from django.shortcuts import render
import xlwt
import os
import json

from django.core.serializers import serialize

from django.http import HttpResponse

from django.core.files import File

from django.shortcuts import get_object_or_404

from .models import InvWatObjLine
from .models import InvWatObjPoly
from .models import InvWatObjPoint
from .models import CatWO
from .models import TargetUseWO
from .models import TargetObosobWOuse
from .models import TargetArendaWO
from .models import ReportTableLand
from .models import FindWO

from .models import Gvk
from .models import Zat
from .models import LineWO
from .models import PointWO
from .models import PolygonWO

from .models import Table1Use
from .models import Table2Obosob
from .models import Table3Arenda

from table import Table1
from table import Table2
from table import Table3
from table import Table4
from table import Table5

from table import Table_use
from table import Table_obosob
from table import Table_arenda

from utils import PagedFilteredTableView

from .filters import ReportTableLandFilter
from .filters import ReportTableFindFilter

from .forms import ObjectsListFormHelper
from .forms import ObjectsListFormHelperFind
from django_tables2 import RequestConfig
from django.shortcuts import redirect


class ReportTableView1(PagedFilteredTableView):
    model = ReportTableLand
    table_class = Table1
    template_name = 'test_table.html'
    paginate_by = 15
    filter_class = ReportTableLandFilter
    formhelper_class = ObjectsListFormHelper
    context_table_name = 'table'  # get error in not avaliable

class ReportTableView2(PagedFilteredTableView):
    model = ReportTableLand
    table_class = Table2
    template_name = 'test_table.html'
    paginate_by = 15
    filter_class = ReportTableLandFilter
    formhelper_class = ObjectsListFormHelper
    context_table_name = 'table'  # get error in not avaliable

class ReportTableView3(PagedFilteredTableView):
    model = ReportTableLand
    table_class = Table3
    template_name = 'test_table.html'
    paginate_by = 15
    filter_class = ReportTableLandFilter
    formhelper_class = ObjectsListFormHelper
    context_table_name = 'table'  # get error in not avaliable

class ReportTableView4(PagedFilteredTableView):
    model = ReportTableLand
    table_class = Table4
    template_name = 'test_table.html'
    paginate_by = 15
    filter_class = ReportTableLandFilter
    formhelper_class = ObjectsListFormHelper
    context_table_name = 'table'  # get error in not avaliable

class ReportTableView5(PagedFilteredTableView):
    model = FindWO
    table_class = Table5
    template_name = 'test_find.html'
    paginate_by = 15
    filter_class = ReportTableFindFilter
    formhelper_class = ObjectsListFormHelperFind
    context_table_name = 'table'  # get error in not avaliable

def get_land(myid):

    print myid
    value_str = ''
    get_obj = Table1Use.objects.all().filter(inv_num=myid)


    for go in get_obj:
        value_str=go.subject

    return value_str


def get_obosob(myid):

    value_str = ''
    get_obj = Table2Obosob.objects.all().filter(inv_num=myid)

    for go in get_obj:
        value_str=go.wateruser

    return value_str

def get_arenda(myid):

    value_str = ''
    get_obj = Table3Arenda.objects.all().filter(inv_num=myid)

    for go in get_obj:
        value_str=go.wateruser

    return value_str

def get_gis_idcatwo_find(myid):

    # получение по myid - индекс категории
    sel_cat =  1

    select_obj = FindWO.objects.all().filter(inv_num=myid)


    for k in select_obj:
        if k.idcatwo in [1,2,3,4,5]:


            sel_cat = 1

            return sel_cat


        if k.idcatwo in [6,7,8,9,10]:

            sel_cat = 2

            return sel_cat


        if k.idcatwo in [11]:

            sel_cat = 3

            return sel_cat

def get_gis_idcatwo(myid):

    # получение по myid - индекс категории
    sel_cat =  1

    select_obj = ReportTableLand.objects.all().filter(inv_num=myid)


    for k in select_obj:
        if k.idcatwo in [1,2,3,4,5]:


            sel_cat = 1

            return sel_cat


        if k.idcatwo in [6,7,8,9,10]:

            sel_cat = 2

            return sel_cat


        if k.idcatwo in [11]:

            sel_cat = 3

            return sel_cat

def get_gis_id_find(myid):

#    выборка по id  ReportTableLand - inv_num

    select_obj = FindWO.objects.all().filter(inv_num=myid)

    sel_new = None

    for k in select_obj:
        if k.idcatwo in [1,2,3,4,5]:


            sel_new = LineWO.objects.all().filter(id_num=myid)

            return sel_new

        if k.idcatwo in [6,7,8,9,10]:

            sel_new = PolygonWO.objects.all().filter(id_num=myid)

            return sel_new


        if k.idcatwo in [11]:

            sel_new = PointWO.objects.all().filter(id_num=myid)

            return sel_new

def get_gis_id(myid):

#    выборка по id  ReportTableLand - inv_num

    select_obj = ReportTableLand.objects.all().filter(inv_num=myid)

    sel_new = None

    for k in select_obj:
        if k.idcatwo in [1,2,3,4,5]:


            sel_new = LineWO.objects.all().filter(id_num=myid)

            return sel_new

        if k.idcatwo in [6,7,8,9,10]:

            sel_new = PolygonWO.objects.all().filter(id_num=myid)

            return sel_new


        if k.idcatwo in [11]:

            sel_new = PointWO.objects.all().filter(id_num=myid)

            return sel_new


def get_context_id_find(myid):

    list = {}

    list_catwo = []
    list_arraytype = []
    list_amount = []
    list_descr = []
    list_name = []

    sel_new = None

#    выборка по id  ReportTableLand - inv_num

    select_obj = FindWO.objects.all().filter(inv_num=myid)

    select_obj1 = Table1Use.objects.all().filter(inv_num=myid)  # will be existing al time
    select_obj2 = Table2Obosob.objects.all().filter(inv_num=myid)  # only several
    select_obj3 = Table3Arenda.objects.all().filter(inv_num=myid)  # only several


    table1_ex = Table_use(select_obj1)
    table2_ex = Table_obosob (select_obj2)
    table3_ex = Table_arenda (select_obj3)

    for k in select_obj:
        list_catwo=k.catwo
        list_arraytype=k.arraytype
        list_amount=k.amount
        list_descr = k.descr_location
        list_name=k.inv_name

    sel_obj = get_gis_id_find(myid)

    cat = get_gis_idcatwo_find(myid)

    print 'id',sel_obj,myid

    if sel_obj != None:
        if cat == 1:
            sel_new = serialize('geojson',sel_obj,geometry_field='line',fields=('name',)) # work only in 1.10 Django
                                                                                      # only line
        if cat == 2:
            sel_new = serialize('geojson', sel_obj, geometry_field='poly', fields=('name',))  # work only in 1.10 Django

        if cat == 3:
            sel_new = serialize('geojson', sel_obj, geometry_field='point', fields=('name',))  # work only in 1.10 Django

        f = open('static/selected.geojson', 'w')
        myfile=File(f)
        myfile.write(sel_new)
        f.closed

    if sel_obj == None:
        f = open('static/selected.geojson', 'w')
        myfile = File(f)
        blank_text=''
        myfile.write(blank_text)
        f.closed

    list = dict([('tab1',table1_ex), ('tab2',table2_ex) , ('tab3',table3_ex) ,('catwo', list_catwo), ('arrayt', list_arraytype),('amount',list_amount),('descr',list_descr),('name',list_name)])

    return list


def get_context_id(myid):

    list = {}

    list_catwo = []
    list_arraytype = []
    list_amount = []
    list_descr = []
    list_name = []

    sel_new = None

#    выборка по id  ReportTableLand - inv_num

    select_obj = ReportTableLand.objects.all().filter(inv_num=myid)

    select_obj1 = Table1Use.objects.all().filter(inv_num=myid)  # will be existing al time
    select_obj2 = Table2Obosob.objects.all().filter(inv_num=myid)  # only several
    select_obj3 = Table3Arenda.objects.all().filter(inv_num=myid)  # only several


    table1_ex = Table_use(select_obj1)
    table2_ex = Table_obosob (select_obj2)
    table3_ex = Table_arenda (select_obj3)

    for k in select_obj:
        list_catwo=k.catwo
        list_arraytype=k.arraytype
        list_amount=k.amount
        list_descr = k.descr_location
        list_name=k.inv_name

    sel_obj = get_gis_id(myid)

    cat = get_gis_idcatwo(myid)

    print 'id',sel_obj,myid

    if sel_obj != None:
        if cat == 1:
            sel_new = serialize('geojson',sel_obj,geometry_field='line',fields=('name',)) # work only in 1.10 Django
                                                                                      # only line
        if cat == 2:
            sel_new = serialize('geojson', sel_obj, geometry_field='poly', fields=('name',))  # work only in 1.10 Django

        if cat == 3:
            sel_new = serialize('geojson', sel_obj, geometry_field='point', fields=('name',))  # work only in 1.10 Django

        f = open('static/selected.geojson', 'w')
        myfile=File(f)
        myfile.write(sel_new)
        f.closed

    if sel_obj == None:
        f = open('static/selected.geojson', 'w')
        myfile = File(f)
        blank_text=''
        myfile.write(blank_text)
        f.closed

    list = dict([('tab1',table1_ex), ('tab2',table2_ex) , ('tab3',table3_ex) ,('catwo', list_catwo), ('arrayt', list_arraytype),('amount',list_amount),('descr',list_descr),('name',list_name)])

    return list


class ReportTableViewDetail(PagedFilteredTableView):
    model = ReportTableLand
    table_class = Table1
    template_name = 'detail_data.html'
    paginate_by = 15
    filter_class = ReportTableLandFilter
    formhelper_class = ObjectsListFormHelper


    def get(self, request, id):

        context = get_context_id(id)

        return render(request,'detail_data.html',context)

class ReportTableFind(PagedFilteredTableView):
    model = FindWO
    template_name = 'detail_data.html'
    paginate_by = 5
    filter_class = ReportTableFindFilter
    formhelper_class = ObjectsListFormHelperFind

    def get(self, request, id):
        context = get_context_id_find(id)

        return render(request, 'detail_data.html', context)


# Create your views here.
def index_view(request):
    template_name= 'index.html'

    return render(request,template_name)

def object_detail(request, id):
    template_name = 'datashow.html'

    return render(request, template_name)

def export_gvk_xls(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="gvk3.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Gvk')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['GVK', 'NPR', 'OKPO', 'NEWOKPO','ZAT_NAME', ]

    for col_num in xrange(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = Gvk.objects.all().distinct('gup').values_list('gup', 'npr', 'okpo', 'newokpo','npr_zat').order_by('gup')

    for row in rows:
        row_num += 1
        for col_num in xrange(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    print 'ok'
    wb.save("gvk3.xls")

    return response

def table_page(request):

    #gvk_obj = Gvk.objects.all().distinct('gup')

    #zat_obj = Zat.objects.all()

    #t = 0

    #for k in zat_obj:

    #    for n in gvk_obj:

    #        if k.kod == n.newokpo and len(k.kod) == len(n.newokpo):
    #            t = t + 1
    #            n.npr_zat = k.npr
    #            n.save(update_fields=['npr_zat'])



    # print request
    # print 'total', t

    #gvk_obj = Gvk.objects.all().distinct('gup')

    #for nn in gvk_obj:
    #    if len(nn.okpo) in [6,7,8]:
    #        nn.newokpo = nn.okpo+nn.ato[0]+'000'
    #        nn.save(update_fields=['newokpo'])
    #    if len(nn.okpo) in [9,10,11,12]:
    #        nn.newokpo = nn.okpo
    #       nn.save(update_fields=['newokpo'])

    #export_gvk_xls(request)

    return render (request, 'table_basic.html')

def show_table(request):

    return render(request, 'table.html')

def get_catwo(id_catwo):

    objcatwo=CatWO.objects.all()

    for k in objcatwo:
        if k.id_catwo== id_catwo:
            return k.catwo_name

def get_typewo(id_typewo):

    objtypewo=TargetUseWO.objects.all()

    for k in objtypewo:
        if k.id_targetusewo == id_typewo:
            return k.targetusewo_name

def get_usetype(array_type):

    Listval=''

    for n in array_type:
        if len(array_type) == 1:
            Listval = get_typewo(n)

        else:
            Listval = Listval+ ',' + get_typewo(n)


    if Listval[0] == ',':
        Listval = Listval[1:]
        return  Listval

    return Listval


def  getlist_byinvnum(in_num):

    list= {}

    wat_obj = None

    select_poly = InvWatObjPoly.objects.all().filter(inv_num=in_num).count()
    if select_poly != 0:
        wat_obj =  InvWatObjPoly.objects.all().filter(inv_num=in_num)
    else:
        select_point = InvWatObjPoint.objects.all().filter(inv_num=in_num).count()
        if select_point != 0:
            wat_obj = InvWatObjPoint.objects.all().filter(inv_num=in_num)
        else:
            select_line = InvWatObjLine.objects.all().filter(inv_num=in_num).count()
            if select_line != 0:
                wat_obj = InvWatObjLine.objects.all().filter(inv_num=in_num)

    list_inv_name=''
    list_idcatwo = 0
    list_amount = 0
    list_descr=''
    list_typearray=[]

    for z_obj in wat_obj:

        list_inv_name = z_obj.inv_name
        list_idcatwo =  z_obj.id_catwo
        list_amount = z_obj.amount
        if z_obj.id_catwo in [1,2,3,4,5]:
            list_descr = z_obj.raion
        else:
            list_descr = z_obj.descr_location
        list_typearray = z_obj.type_array


    list = dict([('inv_name', list_inv_name), ('idcatwo', list_idcatwo), ('amount', list_amount), ('descr', list_descr),
                 ('typearr', list_typearray)])


    return list


def request_page(request):

    value_select = 'no selection'

    result_poly = 0
    result_line = 0
    result_point = 0

    value_select1 = 'no selection'

    value_use=[]

    namewo_obj = []

    catwo_obj = CatWO.objects.all()

    targetusewo_obj = TargetUseWO.objects.all().order_by('id_targetusewo')

    for kk in targetusewo_obj:
         kk.checkin=False
         kk.save(update_fields=['checkin'])

    value_obosob=[]

    targetobosobwuse_obj = TargetObosobWOuse.objects.all().order_by('id_targetobosobwouse')

    for kk in targetobosobwuse_obj:
        kk.checkin = False
        kk.save(update_fields=['checkin'])

    targetarenda_obj = TargetArendaWO.objects.all().order_by('id_targetarendawo')

    for kk in targetarenda_obj:
        kk.checkin = False
        kk.save(update_fields=['checkin'])


    page_num = request.GET.get('page')


    if 'browser' in request.POST:


        listwo = request.POST['browser']
        str_index = listwo.find('#')
        len_listwo = len(listwo)

        if str_index !=-1:
            invnum = int(listwo[str_index+1:len_listwo])



            context = get_context_id(invnum)

            return render(request, 'detail_data.html', context)

    if page_num != None:

        zobjm = TargetUseWO.objects.all()

        amount_wo = 1

        value_records = ReportTableLand.objects.all().count()

        result_polya = InvWatObjPoly.objects.filter(type_array__overlap=value_use).count()
        result_linea = InvWatObjLine.objects.filter(type_array__overlap=value_use).count()
        result_pointa = InvWatObjPoint.objects.filter(type_array__overlap=value_use).count()

        dataLandobj = ReportTableLand.objects.all().order_by('catwo')

        report_table_lake = Table1(dataLandobj)

        tableav=True

        RequestConfig(request, paginate=False).configure(report_table_lake)
        #report_table_lake.paginate(page=request.GET.get('page',3),per_page=15)

        return redirect('/watres/filt/')

        #return render_to_(request,'/',
                   #  {'tableshow':'yes','val_sel2': 'option3_1' ,'res_line':result_linea,'res_poly':result_polya,'res_point':result_pointa,'table':report_table_lake,'tableav':tableav ,'var_use': value_use, 'namewo': namewo_obj,
                   #   'targetusewo': targetusewo_obj})

    if 'radioGroup1' in request.POST:



        #value_select1 = request.POST['radioGroup1']



        if value_select1=='option1_1':
            namewo_obj=InvWatObjLine.objects.all().order_by('inv_name'[:10])

        if value_select1 == 'option1_2':
            namewo_obj = InvWatObjPoly.objects.all().order_by('inv_name'[:10])

        if value_select1 == 'option1_3':
            namewo_obj = InvWatObjPoint.objects.all().order_by('inv_name'[:10])

        return render(request, 'request.html', {'tableshow':'no','val_sel': 'option1', 'val_sel1': value_select1, 'namewo': namewo_obj,'arr_catwo':catwo_obj})

    if 'radioGroup31' in request.POST:

        value_select3 = request.POST['radioGroup31']

        return render(request, 'request.html',
                      {'tableshow':'no','val_sel2': value_select3, 'var_use': value_use, 'namewo': namewo_obj,
                       'targetusewo': targetusewo_obj})


    if 'GetDat1' in request.POST:

        value_obosob = request.POST.getlist('chbox_1')

        zobjm = TargetObosobWOuse.objects.all()

        for vu in value_obosob:
            for zobj in zobjm:

                if str(zobj.id_targetobosobwouse) == vu:
                    if zobj.checkin == True:
                        mm = False
                        zobj.checkin = mm
                        zobj.save(update_fields=['checkin'])
                        break
                    else:
                        mm = True
                        zobj.checkin = mm
                        zobj.save(update_fields=['checkin'])
                        break

        amount_wo = 1

        value_records = ReportTableLand.objects.all().count()

        if value_records != 0:

            ReportTableLand.objects.all().delete()
            # delete records from Model

        targetobosobwuse_obj = TargetObosobWOuse.objects.all().order_by('id_targetobosobwouse')

            # get amount of water objects per value_usecd
        result_obj = Table2Obosob.objects.filter(id_targetwuse__overlap=value_obosob)


        for r_obj in result_obj:
            dataLand = ReportTableLand()
            dataLand.inv_num = r_obj.inv_num # set inv_num
            listin = getlist_byinvnum(r_obj.inv_num)

            dataLand.inv_name = listin.get('inv_name')
            dataLand.catwo = get_catwo(listin.get('idcatwo') )
            dataLand.arraytype=get_usetype(listin.get('typearr'))
            dataLand.obosobtype = r_obj.targetobosobwu
            dataLand.amount = int(listin.get('amount'))
            dataLand.descr_location = listin.get('descr')
            dataLand.idcatwo = int(listin.get('idcatwo'))
            dataLand.save()

        tableav = True

        if page_num == None:
        # report_table_lake.paginate(page=request.GET.get('page',1),per_page=15)

        # return render(request,'request.html',
        #         {'tableshow':'yes','val_sel2': 'option3_1' ,'res_line':result_linea,'res_poly':result_polya,'res_point':result_pointa,'table':report_table_lake,'tableav':tableav ,'var_use': value_use, 'namewo': namewo_obj,
        #        'targetusewo': targetusewo_obj})
            return redirect('/watres/filt2/')

    if 'GetDat2' in request.POST:

        value_arenda = request.POST.getlist('chbox_2')

        zobjm = TargetArendaWO.objects.all()

        for vu in value_arenda:
            for zobj in zobjm:

                if str(zobj.id_targetarendawo) == vu:
                    if zobj.checkin == True:
                        mm = False
                        zobj.checkin = mm
                        zobj.save(update_fields=['checkin'])
                        break
                    else:
                        mm = True
                        zobj.checkin = mm
                        zobj.save(update_fields=['checkin'])
                        break

        amount_wo = 1

        value_records = ReportTableLand.objects.all().count()

        if value_records != 0:
            ReportTableLand.objects.all().delete()
            # delete records from Model

        result_obj = Table3Arenda.objects.filter(id_arenda__overlap=value_arenda)

        for r_obj in result_obj:
            dataLand = ReportTableLand()
            dataLand.inv_num = r_obj.inv_num  # set inv_num
            listin = getlist_byinvnum(r_obj.inv_num)
            dataLand.inv_name = listin.get('inv_name')
            dataLand.catwo = get_catwo(listin.get('idcatwo'))
            dataLand.arraytype=get_usetype(listin.get('typearr'))
            dataLand.areandatype = r_obj.target_ar
            dataLand.amount = int(listin.get('amount'))
            dataLand.descr_location = listin.get('descr')
            dataLand.idcatwo = int(listin.get('idcatwo'))
            dataLand.save()

        tableav = True

        if page_num == None:
            # report_table_lake.paginate(page=request.GET.get('page',1),per_page=15)

            # return render(request,'request.html',
            #         {'tableshow':'yes','val_sel2': 'option3_1' ,'res_line':result_linea,'res_poly':result_polya,'res_point':result_pointa,'table':report_table_lake,'tableav':tableav ,'var_use': value_use, 'namewo': namewo_obj,
            #        'targetusewo': targetusewo_obj})
            return redirect('/watres/filt3/')


    if 'GetData' in request.POST:

        value_select3 = request.POST['GetData']

        value_use = request.POST.getlist('chbox1')

        zobjm = TargetUseWO.objects.all()

        for vu in value_use:
            for zobj in zobjm:

                if str(zobj.id_targetusewo) == vu:
                    if zobj.checkin == True:
                        mm = False
                        zobj.checkin = mm
                        zobj.save(update_fields=['checkin'])
                        break
                    else:
                        mm = True
                        zobj.checkin = mm
                        zobj.save(update_fields=['checkin'])
                        break

        amount_wo = 1

        value_records = ReportTableLand.objects.all().count()

        if value_records != 0:
            ReportTableLand.objects.all().delete()
        # delete records from Model

        targetusewo_obj = TargetUseWO.objects.all().order_by('id_targetusewo')

        result_poly = InvWatObjPoly.objects.filter(type_array__overlap=value_use)
        result_line = InvWatObjLine.objects.filter(type_array__overlap=value_use)
        result_point = InvWatObjPoint.objects.filter(type_array__overlap=value_use)

        for rpoly_obj in result_poly:
            dataLand=ReportTableLand()
            dataLand.inv_num=rpoly_obj.inv_num
            dataLand.inv_name = rpoly_obj.inv_name
            dataLand.catwo=get_catwo(rpoly_obj.id_catwo)
            dataLand.arraytype=get_usetype(rpoly_obj.type_array)
            dataLand.amount=rpoly_obj.amount
            dataLand.descr_location = rpoly_obj.descr_location
            dataLand.idcatwo=rpoly_obj.id_catwo
            dataLand.save()

        for rline_obj in result_line:
            dataLand = ReportTableLand()
            dataLand.inv_num = rline_obj.inv_num
            dataLand.inv_name = rline_obj.inv_name
            dataLand.catwo = get_catwo(rline_obj.id_catwo)
            dataLand.arraytype = get_usetype(rline_obj.type_array)
            dataLand.amount = rline_obj.amount
            dataLand.descr_location = rline_obj.raion
            dataLand.idcatwo = rline_obj.id_catwo
            dataLand.save()

        for rpoint_obj in result_point:
            dataLand = ReportTableLand()
            dataLand.inv_num = rpoint_obj.inv_num
            dataLand.inv_name = rpoint_obj.inv_name
            dataLand.catwo = get_catwo(rpoint_obj.id_catwo)
            dataLand.arraytype = get_usetype(rpoint_obj.type_array)
            dataLand.amount = rpoint_obj.amount
            dataLand.descr_location = rpoint_obj.descr_location
            dataLand.idcatwo = rpoint_obj.id_catwo
            dataLand.save()


        result_polya = InvWatObjPoly.objects.filter(type_array__overlap=value_use).count()
        result_linea = InvWatObjLine.objects.filter(type_array__overlap=value_use).count()
        result_pointa = InvWatObjPoint.objects.filter(type_array__overlap=value_use).count()

        #dataLandobj = ReportTableLand.objects.all().order_by('catwo')

        #report_table_lake = LakeTable(dataLandobj)

        tableav=True

        if page_num == None:
            #report_table_lake.paginate(page=request.GET.get('page',1),per_page=15)

            #return render(request,'request.html',
            #         {'tableshow':'yes','val_sel2': 'option3_1' ,'res_line':result_linea,'res_poly':result_polya,'res_point':result_pointa,'table':report_table_lake,'tableav':tableav ,'var_use': value_use, 'namewo': namewo_obj,
            #        'targetusewo': targetusewo_obj})
            return redirect('/watres/filt1/')

        else:
            print page_num
            #report_table_lake.paginate(page=request.GET.get('page',int(page_num)),per_page=15)

            return render(request,'request.html',
                      {'tableshow':'yes','val_sel2': 'option3_1' ,'res_line':result_linea,'res_poly':result_polya,'res_point':result_pointa,'tableav':tableav ,'var_use': value_use, 'namewo': namewo_obj,
                       'targetusewo': targetusewo_obj})

    if 'chbox1' in request.POST:   # Main use - Table1

        value_use = request.POST.getlist('chbox1')


        zobjm = TargetUseWO.objects.all()

        for vu in value_use:
            for zobj in zobjm:

                if str(zobj.id_targetusewo)==vu:
                    if zobj.checkin==True:
                        mm=False
                        zobj.checkin=mm
                        zobj.save(update_fields=['checkin'])
                        break
                    else:
                        mm=True
                        zobj.checkin=mm
                        zobj.save(update_fields=['checkin'])
                        break

        amount_wo=1

        targetusewo_obj = TargetUseWO.objects.all().order_by('id_targetusewo')

        # get amount of water objects per value_usecd
        result_poly = InvWatObjPoly.objects.filter(type_array__overlap=value_use).count()
        result_line = InvWatObjLine.objects.filter(type_array__overlap=value_use).count()
        result_point = InvWatObjPoint.objects.filter(type_array__overlap=value_use).count()

        return render(request, 'request.html',  {'tableshow':'no','res_line':result_line,'res_poly':result_poly,'res_point':result_point,'val_sel2': 'option3_1', 'var_use': value_use,'namewo': namewo_obj, 'amount': amount_wo ,'targetusewo': targetusewo_obj})

    if 'radio2' in request.POST:   # Obosoblennoj WaterUse

        if request.POST.__getitem__('radio2') == 'use_1': # Obosoblennoj WaterUse

            value_obosob = request.POST.getlist('chbox_1')

            zobjm = TargetObosobWOuse.objects.all()

            for vu in value_obosob:
                for zobj in zobjm:

                    if str(zobj.id_targetobosobwouse) == vu:
                        if zobj.checkin == True:
                            mm = False
                            zobj.checkin = mm
                            zobj.save(update_fields=['checkin'])
                            break
                        else:
                            mm = True
                            zobj.checkin = mm
                            zobj.save(update_fields=['checkin'])
                            break

            amount_wo = 1

            targetobosobwuse_obj = TargetObosobWOuse.objects.all().order_by('id_targetobosobwouse')


            # get amount of water objects per value_usecd
            result_obj = Table2Obosob.objects.filter(id_targetwuse__overlap=value_obosob).count()

            return render(request, 'request.html',
                      {'tableshow': 'no', 'res_point': result_obj,
                       'val_sel2': 'option3_2','val_sel3' : 'use_1', 'var_use': value_use, 'namewo': namewo_obj, 'amount': amount_wo,
                       'targetobosob': targetobosobwuse_obj})

        if request.POST.__getitem__('radio2') == 'use_2': # Arenda

            value_arenda = request.POST.getlist('chbox_2')

            zobjm = TargetArendaWO.objects.all()

            for vu in value_arenda:
                for zobj in zobjm:

                    if str(zobj.id_targetarendawo) == vu:
                        if zobj.checkin == True:
                            mm = False
                            zobj.checkin = mm
                            zobj.save(update_fields=['checkin'])
                            break
                        else:
                            mm = True
                            zobj.checkin = mm
                            zobj.save(update_fields=['checkin'])
                            break

            amount_wo = 1

            targetarenda_obj = TargetArendaWO.objects.all().order_by('id_targetarendawo')


            # get amount of water objects per value_usecd
            result_obj = Table3Arenda.objects.filter(id_arenda__overlap=value_arenda).count()

            return render(request, 'request.html',
                      {'tableshow': 'no', 'res_point': result_obj,
                       'val_sel2': 'option3_2','val_sel3' : 'use_2', 'var_use': value_use, 'namewo': namewo_obj, 'amount': amount_wo,
                       'targetarenda': targetarenda_obj})


        if request.POST.__getitem__('radio2') == 'use_3':  # Arenda

            result_obj = Table3Arenda.objects.filter(id_arenda__overlap=value_arenda)

            return render(request, 'request.html',
                          {'tableshow': 'no', 'res_point': result_obj,
                           'val_sel2': 'option3_2', 'val_sel3': 'use_3', 'var_use': value_use, 'namewo': namewo_obj,
                           'amount': amount_wo,
                           'targetarenda': targetarenda_obj})




    if 'chbox3' in request.POST:
        value_obosob = request.POST['chbox2']

        value_use = request.POST.getlist('chbox1')



    if 'chbox4' in request.POST:
        value_obosob = request.POST['chbox2']

        value_use = request.POST.getlist('chbox1')


    if 'radioGroup' in request.POST:

        value_select = request.POST['radioGroup']



        if value_select == 'option1':

            #FindWO.objects.all().delete()

            value_records = FindWO.objects.all().count()

            if value_records == 0:

                result_poly = InvWatObjPoly.objects.all()
                result_line = InvWatObjLine.objects.all()
                result_point = InvWatObjPoint.objects.all()

                for rpoly_obj in result_poly:
                    dataLand = FindWO()
                    dataLand.inv_num = rpoly_obj.inv_num
                    dataLand.inv_name = rpoly_obj.inv_name
                    dataLand.catwo = get_catwo(rpoly_obj.id_catwo)
                    dataLand.arraytype = get_usetype(rpoly_obj.type_array)
                    dataLand.amount = rpoly_obj.amount
                    dataLand.descr_location = rpoly_obj.descr_location
                    dataLand.idcatwo = rpoly_obj.id_catwo
                    dataLand.sub_land = get_land(rpoly_obj.inv_num)
                    dataLand.sub_arenda =get_arenda(rpoly_obj.inv_num)
                    dataLand.sub_obosob= get_obosob(rpoly_obj.inv_num)
                    dataLand.save()

                for rline_obj in result_line:
                    dataLand = FindWO()
                    dataLand.inv_num = rline_obj.inv_num

                    dataLand.inv_name = rline_obj.inv_name
                    dataLand.catwo = get_catwo(rline_obj.id_catwo)
                    dataLand.arraytype = get_usetype(rline_obj.type_array)
                    dataLand.amount = rline_obj.amount
                    dataLand.descr_location = rline_obj.raion
                    dataLand.idcatwo = rline_obj.id_catwo
                    dataLand.sub_land = get_land(rline_obj.inv_num)
                    dataLand.sub_arenda =get_arenda(rline_obj.inv_num)
                    dataLand.sub_obosob= get_obosob(rline_obj.inv_num)

                    dataLand.save()

                for rpoint_obj in result_point:
                    dataLand = FindWO()
                    dataLand.inv_num = rpoint_obj.inv_num

                    dataLand.inv_name = rpoint_obj.inv_name
                    dataLand.catwo = get_catwo(rpoint_obj.id_catwo)
                    dataLand.arraytype = get_usetype(rpoint_obj.type_array)
                    dataLand.amount = rpoint_obj.amount
                    dataLand.descr_location = rpoint_obj.descr_location
                    dataLand.idcatwo = rpoint_obj.id_catwo
                    dataLand.sub_land = get_land(rpoint_obj.inv_num)
                    dataLand.sub_arenda =get_arenda(rpoint_obj.inv_num)
                    dataLand.sub_obosob= get_obosob(rpoint_obj.inv_num)

                    dataLand.save()

                return redirect('/watres/filt5/')
            return redirect('/watres/filt5/')


        targetusewo_obj = TargetUseWO.objects.all().order_by('id_targetusewo')

        result_poly = 0
        result_line = 0
        result_point = 0

        return render(request, 'request.html', {'tableshow':'no','res_line':result_line,'res_poly':result_poly,'res_point':result_point,'val_sel': value_select ,'var_use': value_use ,'namewo':namewo_obj,'targetusewo':targetusewo_obj})

    else:

        return render(request, 'request.html',{'tableshow':'no','val_sel': value_select})