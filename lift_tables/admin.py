from django.contrib import admin
from lift_tables.models import Competition, Lifter, Result
from django.forms import TextInput, Textarea, Select
from django.db import models

# Register your models here.

class ResultInline(admin.TabularInline):
    model = Result
    extra = 3
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'6'})},
        models.FloatField: {'widget': TextInput(attrs={'size':'6'})},
        models.IntegerField: {'widget': TextInput(attrs={'size':'4'})},
        #models.NullBooleanField: {'widget': Select(attrs={'width':'25'})},
    }

class CompetitionAdmin(admin.ModelAdmin):
    list_display = ( 'date', 'city', 'type' )
    inlines = [ResultInline]
    list_filter = ['date']
    search_fields = ['city', 'type']

class ResultInlineReadonly(admin.TabularInline):
    def get_readonly_fields(self, request, obj=None):
        return list(self.readonly_fields) + \
               [field.name for field in self.model._meta.fields
                if field.name not in self.editable_fields and
                   field.name not in self.exclude]

    def has_add_permission(self, request):
            return False

    def has_delete_permission(self, request):
            return False

    extra = 0
    can_delete = False
    editable_fields = []
    readonly_fields = []
    exclude = []

    model = Result
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'6'})},
        models.FloatField: {'widget': TextInput(attrs={'size':'6'})},
        models.IntegerField: {'widget': TextInput(attrs={'size':'4'})},
    }

class LifterAdmin(admin.ModelAdmin):
    inlines = [ResultInlineReadonly]


admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Lifter, LifterAdmin)
