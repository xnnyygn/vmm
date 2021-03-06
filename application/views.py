from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist, ValidationError
import datetime, logging
from machine.models import MachineTemplate
from application.models import VirtualMachineApplication as VmApplication
from application.models import VirtualMachineApplicationDetail as VmApplicationDetail

logger = logging.getLogger('application')

@login_required
def create(request):
    machine_templates = MachineTemplate.objects.all()
    return __render('application/create.html', {
        'machine_templates': machine_templates}, request, enable_csrf = True)

def __render(template_name, context, request = None, enable_csrf = False):
    if enable_csrf:
        context.update(csrf(request))
        return render(request, template_name, context)
    return render_to_response(template_name, context)

@login_required
def save(request):
    application = VmApplication(proposer = 'xnnyygn', date_applied = datetime.datetime.now())
    application.full_clean()
    application.save()
    machine_template = __get_machine_template(request.POST['machine_template'])
    hostname = __prepare_hostname(request.POST.get('hostname', ''), 
        request.POST.get('hostname_autogenerated', '') == 'true')
    due_date = datetime.datetime.strptime(request.POST['due_date'], '%Y-%m-%d %H:%M:%S')
    detail = VmApplicationDetail(application = application, machine_template = machine_template,
        due_date = due_date, hostname = hostname)
    try:
        # validate
        detail.full_clean()
        detail.save()
    except ValidationError as e:
        logger.warn(e)
        application.delete()
    return redirect('application.views.list')

def __prepare_hostname(user_hostname, auto_generated):
    if auto_generated:
        vm_id = 1
        last_application = VmApplication.objects.order_by('id').reverse()[:1]
        if last_application:
            vm_id = last_application[0].id + 1
        return 'vm%d.xnnyygn.in' % vm_id
    return user_hostname

def __get_machine_template(template_id):
    try:
        return MachineTemplate.objects.get(id = template_id)
    except ObjectDoesNotExist:
        logger.warn('no such machine template [%s]' % template_id)
        return None 

@login_required
def list(request):
    applications = VmApplication.objects.order_by('date_applied').reverse().all()
    summaries = []
    for a in applications:
        summary = {'id': a.id, 'date_applied': a.date_applied}
        machines = []
        for d in a.virtualmachineapplicationdetail_set.all():
            machines.append({
                'template_name': d.machine_template.name,
                'hostname': d.hostname,
                'due_date': d.due_date
            })
        summary['machines'] = machines
        summaries.append(summary)
    return render(request, 'application/list.html', {'summaries': summaries })
