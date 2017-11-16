# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from qsc_food.models import *

# Register your models here.


admin.site.register(Profile)
admin.site.register(Cuisine)
admin.site.register(Food)
admin.site.register(Plate)
admin.site.register(Partition)