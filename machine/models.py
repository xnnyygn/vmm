from django.db import models

class MachineTemplate(models.Model):
    name = models.CharField(max_length = 255) # required
    description = models.TextField()
    planned = models.IntegerField(default = 0)
    used = models.IntegerField(default = 0)

    def __unicode__(self):
        return self.name
