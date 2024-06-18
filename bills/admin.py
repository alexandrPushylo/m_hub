from django.contrib import admin
from bills.models import Electricity, ColdWater, HotWater, Rent, Gas
# Register your models here.

admin.site.register(Electricity)
admin.site.register(ColdWater)
admin.site.register(HotWater)
admin.site.register(Rent)
admin.site.register(Gas)
