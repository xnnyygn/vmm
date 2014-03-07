from django.contrib import admin
from machine.models import MachineTemplate

class MachineTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'planned', 'used')

admin.site.register(MachineTemplate, MachineTemplateAdmin)
