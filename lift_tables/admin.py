from django.contrib import admin
from lift_tables.models import Competition, Lifter, LifterMeta

# Register your models here.
admin.site.register(Competition)
admin.site.register(Lifter)
admin.site.register(LifterMeta)
