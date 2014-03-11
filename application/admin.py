from django.contrib import admin
from application.models import VirtualMachineApplication, VirtualMachineApplicationDetail

class VirtualMachineApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'proposer', 'date_applied')

class VirtualMachineApplicationDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'machine_template', 'due_date', 'hostname')

admin.site.register(VirtualMachineApplication, VirtualMachineApplicationAdmin)
admin.site.register(VirtualMachineApplicationDetail, VirtualMachineApplicationDetailAdmin)
