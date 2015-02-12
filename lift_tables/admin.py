from django.contrib import admin
from lift_tables.models import Competition, PowerLifter, WeightLifter

# Register your models here.
admin.site.register(Competition)
admin.site.register(PowerLifter)
admin.site.register(WeightLifter)
