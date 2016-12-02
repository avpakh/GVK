from django.conf.urls import url,include
from watstat.views import *
from django.contrib import admin

#url(r'^request(?P<page>\d+)/$',request_page),

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^data/',global_page),
    url(r'^dataadm/',data_page),
    url(r'^databasin/',basin_page),
    url(r'^dataecon/',econ_page),

   ]