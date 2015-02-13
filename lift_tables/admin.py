from django.contrib import admin
from lift_tables.models import Competition, Lifter

# Register your models here.

#class LifterMetaAdmin(admin.ModelAdmin):
#    list_display = ( 'date', 'lifter_name', 'competition' )
#
#class LifterAdmin(admin.ModelAdmin):
#    list_display = ( 'name', 'sur_name', 'birthday' )
#
#class CompetitionAdmin(admin.ModelAdmin):
#    list_display = ( 'date', 'type', 'city' )

admin.site.register(Competition)
admin.site.register(Lifter)
#admin.site.register(LifterMeta)
