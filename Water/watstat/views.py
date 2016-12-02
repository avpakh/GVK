# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response
from django.template import RequestContext
import  time
from datetime import datetime,timedelta
from .models import Parameters
from .models import Adm_level
from .models import Basin_level
from .models import Economy_level
from .models import Parameters
from .models import Group
from .models import Datareport
from .table import ReportBasin
from .table import ReportBasinNewTable
from .models import ReportBasinData
from .models import ReportBasinDataNew
import pickle
from django.shortcuts import redirect
from chartit import DataPool,Chart
from django_tables2_reports.config import RequestConfigReport as RequestConfig
from django_tables2_reports.utils import create_report_http_response

import json

basin_lists = []
basin_names = []

param_lists = []
param_names = []

group_lists = []
group_names = []

econ_lists = []
econ_names = []

econ_lists_code = []
econ_lists_name = []

raion_lists_name=[]
raion_lists_code=[]

raion_lists = []
raion_names = []



def json_list(list1,list2):

    lst = []
    for pn in list1:
        d= {}
        d['name']=pn
        v_in = list1.index(pn)
        d['value']=list2[v_in]
        lst.append(d)
    return json.dumps(lst)


def write_list(llist):

    f = open('list.txt', 'w')
    pickle.dump(llist, f)
    return None

def write_params(llist):

    f = open('params.txt', 'w')
    pickle.dump(llist, f)
    return None

def write_names(llist):

    f = open('names.txt', 'w')
    pickle.dump(llist, f)
    return None

def write_param_names(llist):

    f = open('names_p.txt', 'w')
    pickle.dump(llist, f)
    return None

def read_names(nf):
    mynewlist=[]

    with open(nf, 'rb') as f:
        mynewlist = pickle.load(f)
    return mynewlist


def global_page(request):



    return render(request, 'global_data.html')

# Create your views here.

def getSed(invalue):

    value= ''

    value_obj = Economy_level.objects.all().get(kod1=invalue)

    value = value_obj.nai[:8]


    return value

def getval_basin(ya,basin,param):

    value = 0

    val_get = Datareport.objects.all().filter(god=ya).filter(kod=basin)

    for i in val_get:

        value = getattr(i, str(param).lower())

    return value

def econ_page(request):

    show = 0
    error1 = 0
    error = 0

    global econ_lists
    global econ_names
    global econ_lists_name
    global econ_lists_code
    global param_lists
    global param_names

    val_sel = 'no selection'

    if 'GetYears' in request.POST:

        year1 = request.POST.get('year1')
        year2 = request.POST.get('year2')

        print econ_lists

        # 1 Get DataReport records

        reports_obj = Datareport.objects.all().filter(kod__in=econ_lists).filter(god__range=[year1,year2])

        #for param_obj in param_lists:

        value_records =ReportBasinData.objects.all().count()


        if value_records != 0:
            ReportBasinData.objects.all().delete()
            # delete records from Model where will be created a Table

        for r_obj in reports_obj:
            dataBasin = ReportBasinData()

            dataBasin.god = r_obj.god
            dataBasin.kod = r_obj.kod
            dataBasin.nai = r_obj.nai

            for field_param in param_lists:

                if param_lists.index(field_param) == 0:
                    dataBasin.x1=getattr(r_obj,str(param_lists[0].lower()))
                if param_lists.index(field_param) == 1:
                    dataBasin.x2 = getattr(r_obj, str(param_lists[1].lower()))
                if param_lists.index(field_param) == 2:
                    dataBasin.x3 = getattr(r_obj, str(param_lists[2].lower()))
                if param_lists.index(field_param) == 3:
                    dataBasin.x4 = getattr(r_obj, str(param_lists[3].lower()))
                if param_lists.index(field_param) == 4:
                    dataBasin.x5 = getattr(r_obj, str(param_lists[4].lower()))
                if param_lists.index(field_param) == 5:
                    dataBasin.x6 = getattr(r_obj, str(param_lists[5].lower()))
                if param_lists.index(field_param) == 6:
                    dataBasin.x7 = getattr(r_obj, str(param_lists[6].lower()))
                if param_lists.index(field_param) == 7:
                    dataBasin.x8 = getattr(r_obj, str(param_lists[7].lower()))
                if param_lists.index(field_param) == 8:
                    dataBasin.x9 = getattr(r_obj, str(param_lists[8].lower()))
                if param_lists.index(field_param) == 9:
                    dataBasin.x10 = getattr(r_obj, str(param_lists[9].lower()))
                if param_lists.index(field_param) == 10:
                    dataBasin.x11 = getattr(r_obj, str(param_lists[10].lower()))
                if param_lists.index(field_param) == 11:
                    dataBasin.x12 = getattr(r_obj, str(param_lists[11].lower()))

            dataBasin.save()

        dataBasinobj = ReportBasinData.objects.all().order_by('god')

        report_table_basin = ReportBasin(dataBasinobj)

        reports_obj = Datareport.objects.all().filter(kod__in=econ_lists).filter(god__range=[year1, year2])

        value_records = ReportBasinDataNew.objects.all().count()

        if value_records != 0:
            ReportBasinDataNew.objects.all().delete()
            # delete records from Model where will be created a Table

        for b_obj in econ_lists:

            for p_obj in param_lists:

                dataBasin = ReportBasinDataNew()
                       # Set name of basin only once
                dataBasin.nai= econ_names[econ_lists.index(b_obj)]
                dataBasin.param = param_names[param_lists.index(p_obj)]
                dataBasin.x1 = getval_basin(2000,b_obj,p_obj)
                dataBasin.x2 = getval_basin(2001, b_obj, p_obj)
                dataBasin.x3 = getval_basin(2002, b_obj, p_obj)
                dataBasin.x4 = getval_basin(2003, b_obj, p_obj)
                dataBasin.x5 = getval_basin(2004, b_obj, p_obj)
                dataBasin.x6 = getval_basin(2005, b_obj, p_obj)
                dataBasin.x7 = getval_basin(2006, b_obj, p_obj)
                dataBasin.x8 = getval_basin(2007, b_obj, p_obj)
                dataBasin.x9 = getval_basin(2008, b_obj, p_obj)
                dataBasin.x10 = getval_basin(2009, b_obj, p_obj)
                dataBasin.x11 = getval_basin(2010, b_obj, p_obj)
                dataBasin.x12 = getval_basin(2011, b_obj, p_obj)
                dataBasin.x13 = getval_basin(2012, b_obj, p_obj)
                dataBasin.x14 = getval_basin(2013, b_obj, p_obj)
                dataBasin.x15 = getval_basin(2014, b_obj, p_obj)
                dataBasin.x16 = getval_basin(2015, b_obj, p_obj)

                dataBasin.save()

        dataBasinobj = ReportBasinDataNew.objects.all().order_by('nai')

        report_table_basinnew = ReportBasinNewTable(dataBasinobj)

        table_to_report = RequestConfig(request).configure(report_table_basinnew)


        ds=\
            DataPool(
                    series=
                  [{'options': {
                   'source': ReportBasinData.objects.all().order_by('god') },
                  'terms': ['nai','god','x1','x2']}
                   ])

        cht1 = Chart(
                   datasource=ds,
                   series_options=
                    [{'options':{
                     'type': 'column',
                      'stacking': False},'minorTickInterval':'auto',
                      'terms':{
                      'god': ['x1','x2']
                       }},
                          ],
                chart_options=
                     {'chart':
                      {
                       'zoomType': 'x'
                       },
                     'tooltip':{
                      'shared': True,
                      'useHTML': True,
                      'headerFormat': '<small> {point.key}</small><table>',
                       'pointFormat': '<tr><td style="color: {series.color}">{series.name}: </td>' +
                         '<td style="text-align: right"> <b> {point.y}  </b></td></tr>',
                        'footerFormat': '</table>',
                        'valueDecimals': 2
                       },

                    'credits':
                    {
                    'enabled': True
                    },
                    'exporting':
                    {
                    'enabled': True
                    },

                    'title':
                    {
                    'text': ' График  ' + ' ||  '
                    },
                      'colors': ['#34ffff','#349aff','#ff9a34','#ff3434','#35ff34','#9aff34'],

                     'yAxis':
                    {
                    'title' : {'text': ' '},

                   },
                     'navigation': {
                'buttonOptions': {
                'height': 48,
               'width': 48,
                'symbolSize': 24,
                'symbolX': 23,
                'symbolY': 21,
                'symbolStrokeWidth': 2,
                'minorTickInterval':'auto',
                           },
                       },
                     },)

        return render(request, 'table_econ.html', {'dtchart':[cht1],'param': 3, 'basins': econ_names, 'params': param_names,'tab1':report_table_basinnew})


    if 'resultparam1' in request.POST:

        json_str = request.POST.get('resultparam1')

        if len(json_str) != 0:
            error = 0

            python_obj = json.loads(json_str)

            show = len(python_obj)

            param_names=[]
            param_lists=[]

            for k in python_obj:
                param_lists.append(k['value'])
                param_names.append(k['name'])

            return render(request, 'table_econ.html', {'param':2,'basins':econ_names,'params':param_names})


        if len(json_str) == 0:  # if not input but press of button
            error1 = 6

            return render(request, 'table_econ.html', {'error': 6})

    if 'resultgroup' in request.POST:

        json_str = request.POST.get('resultgroup')

        if len(json_str) == 0:
            error1 = 2

            return render(request, 'table_econ.html', {'error1':2})

        if len(json_str) != 0:
            error = 0

            python_obj = json.loads(json_str)

            group_lists=[]
            group_names=[]

            show = len(python_obj)

            for k in python_obj:
                group_lists.append(k['value'])
                group_names.append(k['name'])

              # order per group_name - add

            first_part = []
            second_part = []

            for gr_obj in group_lists:

                param_obj = Parameters.objects.all().exclude(level=1).filter(id_group=gr_obj).order_by('name')

                for obj in param_obj:

                    first_part.append(group_names[group_lists.index(gr_obj)]+' -> '+obj.name)
                    second_part.append(obj.value_field)



            data = json_list(first_part, second_part)

            return render(request, 'table_econ.html', {'dd':data,'param':5,'basins':econ_names,'groups':group_names})

    if 'radioGroupP' in request.POST:

        resp = request.POST['radioGroupP'] # select option1 - option2 - option3 - option4

        if resp == 'chall':

            #basin_names = read_names('names.txt')

            param_obj = Parameters.objects.all().filter(level__in=[2]).order_by('name')  # order per group_name - add

            first_part = []
            second_part = []

            for obj in param_obj:
                first_part.append(obj.name)
                second_part.append(obj.value_field)

            data = json_list(first_part, second_part)


            return render(request, 'table_econ.html', {'dd':data,'param':1,'basins':econ_names,'select':'ok1'})

        if resp == 'chgroup':

            #basin_names = read_names('names.txt')

            group_obj = Group.objects.all().order_by('group_name')  # order per group_name - add

            first_part = []
            second_part = []

            for obj in group_obj:
                first_part.append(obj.group_name)
                second_part.append(obj.id_group)

            data = json_list(first_part, second_part)


            return render(request, 'table_econ.html', {'dd':data,'param':1,'basins':econ_names,'select':'ok2'})


    if 'resultvid' in request.POST:

        json_str = request.POST.get('resultvid')

        econ_lists = []
        econ_names = []

        if len(json_str) != 0:
            error = 0

            python_obj = json.loads(json_str)

            show = len(python_obj)

            for k in python_obj:
                econ_lists.append(k['value'])
                econ_names.append(k['name'])



            # get data for calculation and prepare for next selection
            return render(request, 'table_econ.html', {'param':1,'basins':econ_names,'basins_list':econ_lists,'select':'no'})

        if len(json_str) == 0:  # if not input but press of button
            error1 = 1

            return render(request, 'table_econ.html', {'val_sel': 'error3'})

    if 'GetSection' in request.POST:

        value_obl = request.POST.getlist('chbox_obl3')

        code_list=[]

        econ_lists_name=[]
        econ_lists_code=[]

        for v_obj in value_obl:
            val_code = Economy_level.objects.all().get(pk=v_obj)
            code_list.append(val_code.kod1)

        param_count = Economy_level.objects.all().filter(level__in=[2])

        #print code_list

        for m in code_list:
            sel_econ = param_count.filter(kod0=m)
            #print 'ee',sel_econ
            for rai in sel_econ:
                econ_lists_code.append(rai.kod1)
                namevid = getSed(rai.kod0) + '... -> ' + rai.nai
                econ_lists_name.append(namevid)


        if len(code_list) == 0: # case of error no selected adm. units

            param_obj = Economy_level.objects.all().exclude(nai=u'В С Е   В И Д Ы   ЭКОНОМИЧЕСКОЙ  ДЕЯТЕЛЬНОСТИ').filter(level__in=[1])  # order per group_name - add

            return render(request, 'table_econ.html', {'val_sel': 'error3','dd': param_obj})

        if len(code_list) !=0:

            # write_list(raion_lists)

            # prepare a lists with all raions

            data = json_list(econ_lists_name, econ_lists_code)

            return render(request, 'table_econ.html', {'dd':data,'val_sel': 'Selectedvid'})


    param_obj = Economy_level.objects.all().filter(level__in=[1])

    for kk in param_obj:
        kk.checkin = False
        kk.save(update_fields=['checkin'])

    if 'resultsection' in request.POST:

        json_str = request.POST.get('resultsection')

        econ_lists = []
        econ_names = []

        if len(json_str) != 0:
            error = 0

            python_obj = json.loads(json_str)

            show = len(python_obj)

            for k in python_obj:
                econ_lists.append(k['value'])
                econ_names.append(k['name'])



            # get data for calculation

            return render(request, 'table_econ.html', {'param':1,'basins':econ_names,'basins_list':econ_lists,'select':'no'})



        if len(json_str) == 0:  # if not input but press of button
            error1 = 1

        param_obj = Economy_level.objects.all().filter(level__in=[1])  # order per group_name - add

        first_part = []
        second_part = []

        for obj in param_obj:
            first_part.append(obj.nai)
            second_part.append(obj.kod1)

        data = json_list(first_part, second_part)

        return render(request, 'table_econ.html', {'dd':data,'error': error1, 'val_sel': 'Selected1'})

    if 'radioGroup' in request.POST:

        resp = request.POST['radioGroup'] # select option1 - option2 - option3 - option4

        if resp == 'option1':

            param_obj = Economy_level.objects.all().filter(level__in=[1]).order_by('kod1')  # order per group_name - add

            first_part = []
            second_part = []

            for obj in param_obj:
                first_part.append(obj.nai)
                second_part.append(obj.kod1)

            data = json_list(first_part, second_part)

            return render(request, 'table_econ.html', {'dd':data,'mount':show,'error':error1,'val_sel': 'Selected1'})

        if resp == 'option2':

            param_obj = Economy_level.objects.all().exclude(nai=u'В С Е   В И Д Ы   ЭКОНОМИЧЕСКОЙ  ДЕЯТЕЛЬНОСТИ').filter(level__in=[1]).order_by('kod1')  # order per group_name - add

            return render(request, 'table_econ.html',
                          {'dd': param_obj, 'val_sel': 'Selected3'})

    param_obj = Economy_level.objects.all().filter(level__in=[1]).order_by('kod1')  # order per group_name - add

    first_part = []
    second_part = []

    for obj in param_obj:
        first_part.append(obj.nai)
        second_part.append(obj.kod1)

    data = json_list(first_part, second_part)


    return render(request, 'table_econ.html', {'dd':data,'mount':show,'error':error1,'val_sel': 'no selection'})



def basin_page(request):

    val_sel = 'no selection'

    error = 0
    error1 = 0
    global basin_lists
    global param_lists
    global basin_names
    global param_names
    global group_lists
    global group_names

    if 'GetYears' in request.POST:

        year1 = request.POST.get('year1')
        year2 = request.POST.get('year2')

        # 1 Get DataReport records

        reports_obj = Datareport.objects.all().filter(kod__in=basin_lists).filter(god__range=[year1,year2])

        #for param_obj in param_lists:

        value_records =ReportBasinData.objects.all().count()

        if value_records != 0:
            ReportBasinData.objects.all().delete()
            # delete records from Model where will be created a Table

        for r_obj in reports_obj:
            dataBasin = ReportBasinData()

            dataBasin.god = r_obj.god
            dataBasin.kod = r_obj.kod
            dataBasin.nai = r_obj.nai

            for field_param in param_lists:

                if param_lists.index(field_param) == 0:
                    dataBasin.x1=getattr(r_obj,str(param_lists[0].lower()))
                if param_lists.index(field_param) == 1:
                    dataBasin.x2 = getattr(r_obj, str(param_lists[1].lower()))
                if param_lists.index(field_param) == 2:
                    dataBasin.x3 = getattr(r_obj, str(param_lists[2].lower()))
                if param_lists.index(field_param) == 3:
                    dataBasin.x4 = getattr(r_obj, str(param_lists[3].lower()))
                if param_lists.index(field_param) == 4:
                    dataBasin.x5 = getattr(r_obj, str(param_lists[4].lower()))
                if param_lists.index(field_param) == 5:
                    dataBasin.x6 = getattr(r_obj, str(param_lists[5].lower()))
                if param_lists.index(field_param) == 6:
                    dataBasin.x7 = getattr(r_obj, str(param_lists[6].lower()))
                if param_lists.index(field_param) == 7:
                    dataBasin.x8 = getattr(r_obj, str(param_lists[7].lower()))
                if param_lists.index(field_param) == 8:
                    dataBasin.x9 = getattr(r_obj, str(param_lists[8].lower()))
                if param_lists.index(field_param) == 9:
                    dataBasin.x10 = getattr(r_obj, str(param_lists[9].lower()))
                if param_lists.index(field_param) == 10:
                    dataBasin.x11 = getattr(r_obj, str(param_lists[10].lower()))
                if param_lists.index(field_param) == 11:
                    dataBasin.x12 = getattr(r_obj, str(param_lists[11].lower()))

            dataBasin.save()

        dataBasinobj = ReportBasinData.objects.all().order_by('god')

        report_table_basin = ReportBasin(dataBasinobj)

        reports_obj = Datareport.objects.all().filter(kod__in=basin_lists).filter(god__range=[year1, year2])

        value_records = ReportBasinDataNew.objects.all().count()

        if value_records != 0:
            ReportBasinDataNew.objects.all().delete()
            # delete records from Model where will be created a Table

        for b_obj in basin_lists:

            for p_obj in param_lists:

                dataBasin = ReportBasinDataNew()
                       # Set name of basin only once
                dataBasin.nai= basin_names[basin_lists.index(b_obj)]
                dataBasin.param = param_names[param_lists.index(p_obj)]
                dataBasin.x1 = getval_basin(2000,b_obj,p_obj)
                dataBasin.x2 = getval_basin(2001, b_obj, p_obj)
                dataBasin.x3 = getval_basin(2002, b_obj, p_obj)
                dataBasin.x4 = getval_basin(2003, b_obj, p_obj)
                dataBasin.x5 = getval_basin(2004, b_obj, p_obj)
                dataBasin.x6 = getval_basin(2005, b_obj, p_obj)
                dataBasin.x7 = getval_basin(2006, b_obj, p_obj)
                dataBasin.x8 = getval_basin(2007, b_obj, p_obj)
                dataBasin.x9 = getval_basin(2008, b_obj, p_obj)
                dataBasin.x10 = getval_basin(2009, b_obj, p_obj)
                dataBasin.x11 = getval_basin(2010, b_obj, p_obj)
                dataBasin.x12 = getval_basin(2011, b_obj, p_obj)
                dataBasin.x13 = getval_basin(2012, b_obj, p_obj)
                dataBasin.x14 = getval_basin(2013, b_obj, p_obj)
                dataBasin.x15 = getval_basin(2014, b_obj, p_obj)
                dataBasin.x16 = getval_basin(2015, b_obj, p_obj)

                dataBasin.save()

        dataBasinobj = ReportBasinDataNew.objects.all().order_by('nai')

        report_table_basinnew = ReportBasinNewTable(dataBasinobj)

        table_to_report = RequestConfig(request).configure(report_table_basinnew)

        context =  {'param': 3, 'basins': basin_names, 'params': param_names,}

        #if table_to_report:
        #    return create_report_http_response(table_to_report, request)
        #return render_to_response('table_export.html', {'tab': report_table_basinnew },RequestContext(request,context))

       # ds=\
       #             DataPool(
       #             series=
       #             [{'options': {
       #             'source': ReportBasinData.objects.all().order_by('god') },
       #             'terms': ['nai','god','x1','x2']}
       #             ])

       # cht = Chart(
       #             datasource=ds,
       #             series_options=
       #         [{'options':{
       #           'type': 'column',
       #           'stacking': False},'minorTickInterval':'auto',
       #           'terms':{
       #           'god': ['x1','x2']
       #           }},



       #         ],
       # chart_options=
       #             {'chart':
       #             {
       #             'zoomType': 'x'
       #             },
       #              'tooltip':{
       #               'shared': True,
       #               'useHTML': True,
       #               'headerFormat': '<small> {point.key}</small><table>',
       #                'pointFormat': '<tr><td style="color: {series.color}">{series.name}: </td>' +
       #                  '<td style="text-align: right"> <b> {point.y}  </b></td></tr>',
       #                 'footerFormat': '</table>',
       #                 'valueDecimals': 2
       #                },

       #              'credits':
       #             {
       #             'enabled': True
       #             },
       #              'exporting':
       #             {
       #             'enabled': True
       #             },
       #
       #             'title':
       #             {
       #             'text': '  ' + ' ||  '
       #             },
       #               'colors': ['#34ffff','#349aff','#ff9a34','#ff3434','#35ff34','#9aff34'],

       #              'yAxis':
       #             {
       #             'title' : {'text': ' '},

      #             },
      #               'navigation': {
       #         'buttonOptions': {
       #         'height': 48,
       #        'width': 48,
       #         'symbolSize': 24,
       #         'symbolX': 23,
       #         'symbolY': 21,
       #         'symbolStrokeWidth': 2,
       #         'minorTickInterval':'auto',
       #     },
       #              },

        return render(request, 'table_basin.html', {'param': 3, 'basins': basin_names, 'params': param_names,'tab1':report_table_basinnew})


    if 'resultparam1' in request.POST:

        json_str = request.POST.get('resultparam1')

        if len(json_str) != 0:
            error = 0

            python_obj = json.loads(json_str)

            show = len(python_obj)

            param_names=[]
            param_lists=[]

            for k in python_obj:
                param_lists.append(k['value'])
                param_names.append(k['name'])

            return render(request, 'table_basin.html', {'param':2,'basins':basin_names,'params':param_names})


        if len(json_str) == 0:  # if not input but press of button
            error1 = 1

        basin_obj = Basin_level.objects.all().order_by('nai')  # order per group_name - add

        first_part = []
        second_part = []

        for obj in basin_obj:
            first_part.append(obj.nai)
            second_part.append(obj.kod1)

        data = json_list(first_part, second_part)

        return render(request, 'table_basin.html', {'dd':data,'error': error1, 'val_sel': 'Selected1'})

    if 'resultgroup' in request.POST:

        json_str = request.POST.get('resultgroup')

        if len(json_str) == 0:
            error1 = 2

            return render(request, 'table_basin.html', {'error1':2})

        if len(json_str) != 0:
            error = 0

            python_obj = json.loads(json_str)

            group_lists=[]
            group_names=[]

            show = len(python_obj)

            for k in python_obj:
                group_lists.append(k['value'])
                group_names.append(k['name'])

              # order per group_name - add

            first_part = []
            second_part = []

            for gr_obj in group_lists:

                param_obj = Parameters.objects.all().exclude(level=1).filter(id_group=gr_obj).order_by('name')

                for obj in param_obj:

                    first_part.append(group_names[group_lists.index(gr_obj)]+' -> '+obj.name)
                    second_part.append(obj.value_field)



            data = json_list(first_part, second_part)

            return render(request, 'table_basin.html', {'dd':data,'param':5,'basins':basin_names,'groups':group_names})

    if 'radioGroupP' in request.POST:

        resp = request.POST['radioGroupP'] # select option1 - option2 - option3 - option4

        if resp == 'chall':

            #basin_names = read_names('names.txt')

            param_obj = Parameters.objects.all().filter(level__in=[2]).order_by('name')  # order per group_name - add

            first_part = []
            second_part = []

            for obj in param_obj:
                first_part.append(obj.name)
                second_part.append(obj.value_field)

            data = json_list(first_part, second_part)


            return render(request, 'table_basin.html', {'dd':data,'param':1,'basins':basin_names,'select':'ok1'})

        if resp == 'chgroup':

            #basin_names = read_names('names.txt')

            group_obj = Group.objects.all().order_by('group_name')  # order per group_name - add

            first_part = []
            second_part = []

            for obj in group_obj:
                first_part.append(obj.group_name)
                second_part.append(obj.id_group)

            data = json_list(first_part, second_part)


            return render(request, 'table_basin.html', {'dd':data,'param':1,'basins':basin_names,'select':'ok2'})

    if 'resultbasin' in request.POST:

        json_str = request.POST.get('resultbasin')

        if len(json_str) != 0:
            error = 0

            python_obj = json.loads(json_str)

            basin_lists=[]
            basin_names=[]

            show = len(python_obj)

            for k in python_obj:
                basin_lists.append(k['value'])
                basin_names.append(k['name'])


            #write_list(basin_lists)
            #write_names(basin_names)

            return render(request, 'table_basin.html', {'param':1,'basins':basin_names,'basins_list':basin_lists,'select':'no'})


        if len(json_str) == 0:  # if not input but press of button

            error1 = 1

            basin_obj = Basin_level.objects.all().order_by('nai')  # order per group_name - add

            first_part = []
            second_part = []

            for obj in basin_obj:
                first_part.append(obj.nai)
                second_part.append(obj.kod1)

            data = json_list(first_part, second_part)

            return render(request, 'table_basin.html', {'dd':data,'error': error1, 'param': 0})



    basin_obj = Basin_level.objects.all().order_by('nai')

    first_part = []
    second_part = []

    for obj in basin_obj:
        first_part.append(obj.nai)
        second_part.append(obj.kod1)


    data = json_list(first_part,second_part)

    return render (request,'table_basin.html',{'dd':data,'error':error,'param':0})


def data_page(request):

    show = 0
    error1 = 0
    error2 = 0
    error = 0

    val_sel = 'no selection'

    global raion_lists
    global raion_names
    global raion_lists_code
    global raion_lists_name
    global param_lists
    global param_names

    if 'GetYears' in request.POST:

        year1 = request.POST.get('year1')
        year2 = request.POST.get('year2')


        # 1 Get DataReport records

        reports_obj = Datareport.objects.all().filter(kod__in=raion_lists).filter(god__range=[year1,year2])

        #for param_obj in param_lists:

        value_records =ReportBasinData.objects.all().count()


        if value_records != 0:
            ReportBasinData.objects.all().delete()
            # delete records from Model where will be created a Table

        for r_obj in reports_obj:
            dataBasin = ReportBasinData()

            dataBasin.god = r_obj.god
            dataBasin.kod = r_obj.kod
            dataBasin.nai = r_obj.nai

            for field_param in param_lists:

                if param_lists.index(field_param) == 0:
                    dataBasin.x1=getattr(r_obj,str(param_lists[0].lower()))
                if param_lists.index(field_param) == 1:
                    dataBasin.x2 = getattr(r_obj, str(param_lists[1].lower()))
                if param_lists.index(field_param) == 2:
                    dataBasin.x3 = getattr(r_obj, str(param_lists[2].lower()))
                if param_lists.index(field_param) == 3:
                    dataBasin.x4 = getattr(r_obj, str(param_lists[3].lower()))
                if param_lists.index(field_param) == 4:
                    dataBasin.x5 = getattr(r_obj, str(param_lists[4].lower()))
                if param_lists.index(field_param) == 5:
                    dataBasin.x6 = getattr(r_obj, str(param_lists[5].lower()))
                if param_lists.index(field_param) == 6:
                    dataBasin.x7 = getattr(r_obj, str(param_lists[6].lower()))
                if param_lists.index(field_param) == 7:
                    dataBasin.x8 = getattr(r_obj, str(param_lists[7].lower()))
                if param_lists.index(field_param) == 8:
                    dataBasin.x9 = getattr(r_obj, str(param_lists[8].lower()))
                if param_lists.index(field_param) == 9:
                    dataBasin.x10 = getattr(r_obj, str(param_lists[9].lower()))
                if param_lists.index(field_param) == 10:
                    dataBasin.x11 = getattr(r_obj, str(param_lists[10].lower()))
                if param_lists.index(field_param) == 11:
                    dataBasin.x12 = getattr(r_obj, str(param_lists[11].lower()))

            dataBasin.save()

        dataBasinobj = ReportBasinData.objects.all().order_by('god')

        report_table_basin = ReportBasin(dataBasinobj)

        reports_obj = Datareport.objects.all().filter(kod__in=raion_lists).filter(god__range=[year1, year2])



        value_records = ReportBasinDataNew.objects.all().count()

        if value_records != 0:
            ReportBasinDataNew.objects.all().delete()
            # delete records from Model where will be created a Table

        for b_obj in raion_lists:

            for p_obj in param_lists:

                dataBasin = ReportBasinDataNew()
                       # Set name of basin only once
                dataBasin.nai= raion_names[raion_lists.index(b_obj)]
                dataBasin.param = param_names[param_lists.index(p_obj)]
                dataBasin.x1 = getval_basin(2000,b_obj,p_obj)
                dataBasin.x2 = getval_basin(2001, b_obj, p_obj)
                dataBasin.x3 = getval_basin(2002, b_obj, p_obj)
                dataBasin.x4 = getval_basin(2003, b_obj, p_obj)
                dataBasin.x5 = getval_basin(2004, b_obj, p_obj)
                dataBasin.x6 = getval_basin(2005, b_obj, p_obj)
                dataBasin.x7 = getval_basin(2006, b_obj, p_obj)
                dataBasin.x8 = getval_basin(2007, b_obj, p_obj)
                dataBasin.x9 = getval_basin(2008, b_obj, p_obj)
                dataBasin.x10 = getval_basin(2009, b_obj, p_obj)
                dataBasin.x11 = getval_basin(2010, b_obj, p_obj)
                dataBasin.x12 = getval_basin(2011, b_obj, p_obj)
                dataBasin.x13 = getval_basin(2012, b_obj, p_obj)
                dataBasin.x14 = getval_basin(2013, b_obj, p_obj)
                dataBasin.x15 = getval_basin(2014, b_obj, p_obj)
                dataBasin.x16 = getval_basin(2015, b_obj, p_obj)

                dataBasin.save()

        dataBasinobj = ReportBasinDataNew.objects.all().order_by('nai')

        report_table_basinnew = ReportBasinNewTable(dataBasinobj)

        table_to_report = RequestConfig(request).configure(report_table_basinnew)


       # ds=\
       #             DataPool(
       #             series=
       #             [{'options': {
       #             'source': ReportBasinData.objects.all().order_by('god') },
       #             'terms': ['nai','god','x1','x2']}
       #             ])

       # cht = Chart(
       #             datasource=ds,
       #             series_options=
       #         [{'options':{
       #           'type': 'column',
       #           'stacking': False},'minorTickInterval':'auto',
       #           'terms':{
       #           'god': ['x1','x2']
       #           }},



       #         ],
       # chart_options=
       #             {'chart':
       #             {
       #             'zoomType': 'x'
       #             },
       #              'tooltip':{
       #               'shared': True,
       #               'useHTML': True,
       #               'headerFormat': '<small> {point.key}</small><table>',
       #                'pointFormat': '<tr><td style="color: {series.color}">{series.name}: </td>' +
       #                  '<td style="text-align: right"> <b> {point.y}  </b></td></tr>',
       #                 'footerFormat': '</table>',
       #                 'valueDecimals': 2
       #                },

       #              'credits':
       #             {
       #             'enabled': True
       #             },
       #              'exporting':
       #             {
       #             'enabled': True
       #             },
       #
       #             'title':
       #             {
       #             'text': '  ' + ' ||  '
       #             },
       #               'colors': ['#34ffff','#349aff','#ff9a34','#ff3434','#35ff34','#9aff34'],

       #              'yAxis':
       #             {
       #             'title' : {'text': ' '},

      #             },
      #               'navigation': {
       #         'buttonOptions': {
       #         'height': 48,
       #        'width': 48,
       #         'symbolSize': 24,
       #         'symbolX': 23,
       #         'symbolY': 21,
       #         'symbolStrokeWidth': 2,
       #         'minorTickInterval':'auto',
       #     },
       #              },

        return render(request, 'table_data.html', {'param': 3, 'basins': raion_names, 'params': param_names,'tab1':report_table_basinnew})


    if 'resultparam1' in request.POST:

        json_str = request.POST.get('resultparam1')

        if len(json_str) != 0:
            error = 0

            python_obj = json.loads(json_str)

            show = len(python_obj)

            param_names=[]
            param_lists=[]

            for k in python_obj:
                param_lists.append(k['value'])
                param_names.append(k['name'])

            return render(request, 'table_data.html', {'param':2,'basins':raion_names,'params':param_names})


        if len(json_str) == 0:  # if not input but press of button
            error1 = 6

            return render(request, 'table_data.html', {'error': 6})

    if 'resultgroup' in request.POST:

        json_str = request.POST.get('resultgroup')

        if len(json_str) == 0:
            error1 = 2

            return render(request, 'table_data.html', {'error1':2})

        if len(json_str) != 0:
            error = 0

            python_obj = json.loads(json_str)

            group_lists=[]
            group_names=[]

            show = len(python_obj)

            for k in python_obj:
                group_lists.append(k['value'])
                group_names.append(k['name'])

              # order per group_name - add

            first_part = []
            second_part = []

            for gr_obj in group_lists:

                param_obj = Parameters.objects.all().exclude(level=1).filter(id_group=gr_obj).order_by('name')

                for obj in param_obj:

                    first_part.append(group_names[group_lists.index(gr_obj)]+' -> '+obj.name)
                    second_part.append(obj.value_field)



            data = json_list(first_part, second_part)

            return render(request, 'table_data.html', {'dd':data,'param':5,'basins':raion_names,'groups':group_names})

    if 'radioGroupP' in request.POST:

        resp = request.POST['radioGroupP'] # select option1 - option2 - option3 - option4

        if resp == 'chall':

            #basin_names = read_names('names.txt')

            param_obj = Parameters.objects.all().filter(level__in=[2]).order_by('name')  # order per group_name - add

            first_part = []
            second_part = []

            for obj in param_obj:
                first_part.append(obj.name)
                second_part.append(obj.value_field)

            data = json_list(first_part, second_part)


            return render(request, 'table_econ.html', {'dd':data,'param':1,'basins':raion_names,'select':'ok1'})

        if resp == 'chgroup':

            #basin_names = read_names('names.txt')

            group_obj = Group.objects.all().order_by('group_name')  # order per group_name - add

            first_part = []
            second_part = []

            for obj in group_obj:
                first_part.append(obj.group_name)
                second_part.append(obj.id_group)

            data = json_list(first_part, second_part)


            return render(request, 'table_econ.html', {'dd':data,'param':1,'basins':raion_names,'select':'ok2'})








    if 'result3select' in request.POST:

        json_str = request.POST.get('result3select')

        raion_lists = []
        raion_names=  []

        if len(json_str) != 0:
            error = 0

            python_obj = json.loads(json_str)

            show = len(python_obj)

            for k in python_obj:
                raion_lists.append(k['value'])
                raion_names.append(k['name'])



            # get data for calculation and prepare for next selection

            return render(request, 'table_data.html', {'param':1,'basins':raion_names,'basins_list':raion_lists,'select':'no'})


        if len(json_str) == 0:  # if not input but press of button
            error1 = 1

            return render(request, 'table_data.html', {'val_sel': 'error3'})

    if 'result4select' in request.POST:

        json_str = request.POST.get('result4select')

        raion_lists = []
        raion_names = []

        if len(json_str) != 0:
            error = 0

            python_obj = json.loads(json_str)

            show = len(python_obj)

            for k in python_obj:
                raion_lists.append(k['value'])
                raion_names.append(k['name'])



            # get data for calculation and prepare for next selection
            return render(request, 'table_data.html', {'param':1,'basins':raion_names,'basins_list':raion_lists,'select':'no'})


        if len(json_str) == 0:  # if not input but press of button
            error1 = 1

            return render(request, 'table_data.html', {'val_sel': 'error4'})

    if 'GetOblRaion' in request.POST:

        value_obl = request.POST.getlist('chbox_obl3')

        code_list=[]

        raion_lists_name=[]
        raion_lists_code=[]

        for v_obj in value_obl:
            val_code = Adm_level.objects.all().get(pk=v_obj)
            code_list.append(val_code.code)

        param_count = Adm_level.objects.all().filter(level__in=[4])

        for m in code_list:
            sel_raions = param_count.filter(code__startswith=m)
            for rai in sel_raions:
                raion_lists_code.append(rai.code)
                raion_lists_name.append(rai.name)


        if len(code_list) == 0: # case of error no selected adm. units

            param_obj = Adm_level.objects.all().filter(level__in=[2])  # order per group_name - add

            return render(request, 'table_data.html', {'val_sel': 'error','dd': param_obj})

        if len(code_list) !=0:

            # write_list(raion_lists)

            # prepare a lists with all raions

            data = json_list(raion_lists_name, raion_lists_code)

            return render(request, 'table_data.html', {'dd':data,'val_sel': 'Selected3r'})


    if 'GetOblCity' in request.POST:

        value_obl = request.POST.getlist('chbox_obl')

        code_list=[]

        raion_lists_name=[]
        raion_lists_code=[]

        for v_obj in value_obl:
            val_code = Adm_level.objects.all().get(pk=v_obj)
            code_list.append(val_code.code)

        param_count = Adm_level.objects.all().filter(level__in=[6])

        for m in code_list:
            sel_raions = param_count.filter(code__startswith=m)
            for rai in sel_raions:
                raion_lists_code.append(rai.code)
                raion_lists_name.append(rai.name)


        if len(code_list) == 0: # case of error no selected adm. units

            param_obj = Adm_level.objects.all().filter(level__in=[2])  # order per group_name - add

            return render(request, 'table_data.html', {'val_sel': 'error','dd': param_obj})

        if len(code_list) !=0:

            # write_list(raion_lists)

            # prepare a lists with all raions

            data = json_list(raion_lists_name, raion_lists_code)

            return render(request, 'table_data.html', {'dd':data,'val_sel': 'Selected4r'})

    param_obj = Adm_level.objects.all().filter(level__in=[1, 2])

    for kk in param_obj:
        kk.checkin = False
        kk.save(update_fields=['checkin'])

    if 'result1' in request.POST:

        json_str = request.POST.get('result1')

        raion_lists = []
        raion_names = []

        if len(json_str) != 0:
            error = 0

            python_obj = json.loads(json_str)

            show = len(python_obj)

            for k in python_obj:
                raion_lists.append(k['value'])
                raion_names.append(k['name'])



            return render(request, 'table_data.html', {'param':1,'basins':raion_names,'basins_list':raion_lists,'select':'no'})

            # get data for calculation

        if len(json_str) == 0:  # if not input but press of button
            error1 = 1

        param_obj = Adm_level.objects.all().filter(level__in=[1, 2])  # order per group_name - add

        first_part = []
        second_part = []

        for obj in param_obj:
            first_part.append(obj.name)
            second_part.append(obj.code)

        data = json_list(first_part, second_part)

        return render(request, 'table_data.html', {'dd':data,'error': error1, 'val_sel': 'Selected1'})

    if 'result2' in request.POST:

        json_str = request.POST.get('result2')

        raion_lists = []
        raion_names = []


        if len(json_str) != 0:
            error = 0

            python_obj = json.loads(json_str)

            show = len(python_obj)

            for k in python_obj:
                raion_lists.append(k['value'])
                raion_names.append(k['name'])



            return render(request, 'table_data.html', {'param':1,'basins':raion_names,'basins_list':raion_lists,'select':'no'})

            # get data for calculation

        if len(json_str) == 0:  # if not input but press of button
            error1 = 1

        param_obj = Adm_level.objects.all().filter(level__in=[3, 5])  # order per group_name - add

        first_part = []
        second_part = []

        for obj in param_obj:
            first_part.append(obj.name)
            second_part.append(obj.code)

        data = json_list(first_part, second_part)

        return render(request, 'table_data.html', {'dd': data, 'error': error1, 'val_sel': 'Selected2'})

    if 'result4r' in request.POST:

        json_str = request.POST.get('result4r')

        raion_lists = []
        raion_names = []


        if len(json_str) != 0:
            error = 0

            python_obj = json.loads(json_str)

            show = len(python_obj)

            for k in python_obj:
                raion_lists.append(k['value'])
                raion_names.append(k['name'])


            return render(request, 'table_data.html', {'param':1,'basins':raion_names,'basins_list':raion_lists,'select':'no'})

            # get data for calculation

        if len(json_str) == 0:  # if not input but press of button
            error1 = 1

        param_obj = Adm_level.objects.all().filter(level__in=[6])  # order per group_name - add

        first_part = []
        second_part = []

        for obj in param_obj:
            first_part.append(obj.name)
            second_part.append(obj.code)

        data = json_list(first_part, second_part)

        return render(request, 'table_data.html', {'dd': data, 'error': error1, 'val_sel': 'Selected4'})

    if 'radioGroup' in request.POST:

        resp = request.POST['radioGroup'] # select option1 - option2 - option3 - option4

        if resp == 'option1':

            param_obj = Adm_level.objects.all().filter(level__in=[1, 2]).order_by('code')  # order per group_name - add

            first_part = []
            second_part = []

            for obj in param_obj:
                first_part.append(obj.name)
                second_part.append(obj.code)

            data = json_list(first_part, second_part)


            return render(request, 'table_data.html', {'dd':data,'mount':show,'error':error1,'val_sel': 'Selected1'})

        if resp == 'option2':

            param_obj = Adm_level.objects.all().filter(level__in=[3, 5]).order_by('code') # order per group_name - add

            first_part = []
            second_part = []

            for obj in param_obj:
                first_part.append(obj.name)
                second_part.append(obj.code)

            data = json_list(first_part, second_part)

            return render(request, 'table_data.html', {'dd': data, 'mount': show, 'error': error2, 'val_sel': 'Selected2'})

        if resp == 'option3':

            param_obj = Adm_level.objects.all().filter(level__in=[2]).order_by('code')  # order per group_name - add

            return render(request, 'table_data.html',
                          {'dd': param_obj, 'val_sel': 'Selected3'})

        if resp == 'option4':

            param_obj = Adm_level.objects.all().exclude(name=u'г МИНСК').filter(level__in=[2]).order_by('code')  # order per group_name - add

            return render(request, 'table_data.html',
                          {'dd': param_obj, 'val_sel': 'Selected4'})

    if 'result' in request.POST:

        json_str = request.POST.get('result')

        if len(json_str) !=0:

            python_obj = json.loads(json_str)

            show=len(python_obj)

            error=0

        if len(json_str) == 0: # if not input but press of button

            error = 1


    param_obj = Adm_level.objects.all().filter(level__in=[3,5]) # order per group_name - add

    first_part = []
    second_part = []

    for obj in param_obj:
        first_part.append(obj.name)
        second_part.append(obj.code)


    data = json_list(first_part,second_part)


    return render (request,'table_data.html',{'dd':data,'mount':show,'error':error,'val_sel':val_sel})