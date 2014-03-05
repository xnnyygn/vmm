from django.db import models
from django.contrib import admin

class Application(models.Model):
	# just user name
	proposer = models.CharField(max_length = 255)
	date_applied = models.DateTimeField(auto_now = True)

class MachineTemplate(models.Model):
	name = models.CharField(max_length = 255)
	description = models.TextField()
	total = models.IntegerField()
	remaining = models.IntegerField()

class MachineTemplateAdmin(admin.ModelAdmin):
	list_display = ('name', 'total', 'remaining')

class ApplicationDetail(models.Model):
	application = models.ForeignKey(Application)
	template = models.ForeignKey(MachineTemplate)
	count = models.IntegerField()

class MachineUsage(models.Model):
	application = models.ForeignKey(Application)
	date_actived = models.DateTimeField(auto_now = True)
	due_date = models.DateTimeField()
	hostname = models.CharField(max_length = 255)
	ip = models.CharField(max_length = 64)

admin.site.register(MachineTemplate, MachineTemplateAdmin)
