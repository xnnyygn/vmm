from django.db import models
from machine.models import MachineTemplate

class VirtualMachineApplication(models.Model):
    proposer = models.CharField(max_length = 255)
    date_applied = models.DateTimeField()

    def __unicode__(self):
        return 'application#%d' % self.id

class VirtualMachineApplicationDetail(models.Model):
    application = models.ForeignKey(VirtualMachineApplication)
    due_date = models.DateTimeField()
    machine_template = models.ForeignKey(MachineTemplate)
    hostname = models.CharField(max_length = 255)
