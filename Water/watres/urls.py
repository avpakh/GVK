from django.conf.urls import url,include
from watres.views import *
from django.contrib import admin

#url(r'^request(?P<page>\d+)/$',request_page),

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tables/',table_page),
    url(r'^request/',request_page),
    url(r'^filt1/', ReportTableView1.as_view(), name='test_table'),
    url(r'^filt2/', ReportTableView2.as_view(), name='test_table'),
    url(r'^filt3/', ReportTableView3.as_view(), name='test_table'),
    url(r'^filt4/', ReportTableView4.as_view(), name='test_table'),
    url(r'^filt5/', ReportTableView5.as_view(), name='test_table'),
    url(r'new/(\d+)/', ReportTableViewDetail.as_view(), name='object_detail'),
    url(r'find/(\d+)/', ReportTableFind.as_view(), name='object_find'),
   ]