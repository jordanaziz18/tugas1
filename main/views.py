from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from main.models import tokocamera
from main.forms import tokocameraform

def show_main(request):
    context = {
        'name': 'Muhammad Jordan ',
        'class': 'PBP KKI'
    }

    return render(request, "main.html", context)

def create_camera_entry(request):
    form = tokocameraform()

    if request.method == 'POST':
        form = tokocameraform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:show_main')
        
    context = {'form': form}
    return render(request, 'create_bacon_entry.html', context)

def show_xml(request):
    data = tokocamera.objects.all()
    return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')

def show_json(request):
    data = tokocamera.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

def show_xml_by_id(request, id):
    data = tokocamera.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')

def show_json_by_id(request, id):
    data = tokocamera.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

