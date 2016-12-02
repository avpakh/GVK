# -*- coding: utf-8 -*-

from .models import ReportTableLand
from .models import FindWO
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Button


class ObjectsListFormHelper(FormHelper):
    model = ReportTableLand
    form_show_errors = False
    form_error_title = False
    help_text_inline = True
    html5_required = True
    form_tag = True
    form_class = 'form-inline'
    layout = Layout('catwo','descr_location','inv_name',ButtonHolder(
        Submit('submit', u'Применить фильтры', css_class='btn-primary ',),

                 ))

class ObjectsListFormHelperFind(FormHelper):
    model = FindWO
    form_show_errors = False
    form_error_title = False
    help_text_inline = True
    html5_required = True
    form_tag = True
    form_class = 'form-inline'
    layout = Layout('catwo','descr_location','inv_name','sub_land','sub_obosob','sub_arenda',ButtonHolder(
        Submit('submit', u'Осуществить запрос ', css_class='btn-primary ',),

                 ))
