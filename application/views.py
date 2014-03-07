from django.shortcuts import render_to_response
from machine.models import MachineTemplate

def create(request):
    machine_templates = MachineTemplate.objects.all()
    return render_to_response('application/create.html', {
        'machine_templates': machine_templates
    })
