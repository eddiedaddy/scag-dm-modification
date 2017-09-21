# coding=utf-8

# UrbanFootprint v1.5
# Copyright (C) 2016 Calthorpe Analytics
#
# This file is part of UrbanFootprint version 1.5
#
# UrbanFootprint is distributed under the terms of the GNU General
# Public License version 3, as published by the Free Software Foundation. This
# code is distributed WITHOUT ANY WARRANTY, without implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License v3 for more details; see <http://www.gnu.org/licenses/>.

from django.contrib.gis.db import models
from footprint.main.models.geospatial.feature import Feature

__author__ = 'calthorpe_analytics'


class CpadHoldings(Feature):
    agency_name = models.CharField(max_length=100, null=True, blank=True)
    county = models.CharField(max_length=100, null=True, blank=True)
    agency_lev = models.CharField(max_length=100, null=True, blank=True)
    mng_agency = models.CharField(max_length=100, null=True, blank=True)
    own_type = models.CharField(max_length=100, null=True, blank=True)
    site_name = models.CharField(max_length=100, null=True, blank=True)
    hold_notes = models.CharField(max_length=320, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    desg_agncy = models.CharField(max_length=100, null=True, blank=True)
    desg_nat = models.CharField(max_length=100, null=True, blank=True)
    layer = models.CharField(max_length=100, null=True, blank=True)
    layer_scag = models.CharField(max_length=100, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    notes = models.CharField(max_length=1024, null=True, blank=True)


    class Meta(object):
        abstract = True
        app_label = 'main'
