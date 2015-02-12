from django.contrib import admin
from lift_tables.models import Competition, Lifter, LifterMeta

# Register your models here.

class LifterMetaAdmin(admin.ModelAdmin):
    list_display = ( 'date', 'lifter_name', 'competition' )

class LifterAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'sur_name', 'birthday' )

class CompetitionAdmin(admin.ModelAdmin):
    list_display = ( 'date', 'type', 'city', 'country_code' )

admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Lifter, LifterAdmin)
admin.site.register(LifterMeta, LifterMetaAdmin)
