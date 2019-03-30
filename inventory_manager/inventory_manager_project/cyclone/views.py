# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from cyclone.models import arrays, employees
from cyclone.forms import arrays_form, arrays_release_form
from django.http import HttpResponseRedirect,HttpResponse

from django.shortcuts import render

# Create your views here.
def main(request):

    form = arrays_form(request.POST or None)
    form_release = arrays_release_form(request.POST or None)
    if request.POST:
        input = request.POST['array_name']
        instance = arrays.objects.get(array_name=input)
        form = arrays_form(request.POST, instance = instance)
        form_release = arrays_release_form(request.POST, instance=instance)
        if form.is_valid():
            save_it = form.save(commit=False)
            save_it.array_status = True
            form.save()
            return HttpResponseRedirect(request.path_info)
        elif form_release.is_valid():
            save_it = form_release.save(commit=False)
            save_it.array_status = False
            save_it.employee_array = employees.objects.get(employee_id="-")
            form_release.save()
            return HttpResponseRedirect(request.path_info)

    all_arrays = arrays.objects.order_by('array_status')
    all_employees = employees.objects.all()
    available_arrays = arrays.objects.filter(array_status=False)
    resouce_utilization = (float(len(all_arrays) - len(available_arrays))/float(len(all_arrays)))*100
    resouce_utilization= format(resouce_utilization,'.2f')
    context={'arrays':all_arrays, 'employees':all_employees, 'available_arrays':available_arrays,
             'resouce_utilization':resouce_utilization,
             'form':form, 'form2':form_release}
    return render(request, 'base.html', context=context)
