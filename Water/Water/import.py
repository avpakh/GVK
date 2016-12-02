# -*- coding: utf-8 -*-

import os
import watres

from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.utils import LayerMapping

from watres.models import TestGeo, testgeo_mapping

class Command(BaseCommand):
    help = 'Loads additional shape data from app data directory'

    def handle(self, *args, **options):
        unit_shp = os.path.abspath(os.path.join(os.path.join(os.path.dirname(watres.__file__), 'Export_Output_2.shp')))

        lm = LayerMapping(TestGeo, unit_shp, testgeo_mapping,
            transform=False, encoding='iso-8859-1')
        lm.save(strict=True, verbose=True)
