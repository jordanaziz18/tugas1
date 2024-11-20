from django.shortcuts import render, redirect
from django.core import serializers
from main.models import tokocamera
from main.forms import tokocameraform
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, Http404, HttpResponse, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags




@login_required(login_url='/login')
def show_main(request):
    camera_entries = tokocamera.objects.filter(user=request.user)
    context = {
        'name': request.user.username,
        'last_login': request.COOKIES.get('last_login'),
        'class': 'PBP KKI',
        'camera_entries': camera_entries,  # Include camera entries in context
    }
    return render(request, "main.html", context)

def create_camera_entry(request):
    form = tokocameraform(request.POST or None)

    if form.is_valid() and request.method == "POST":
            camera_entry = form.save(commit=False)
            camera_entry.user = request.user
            camera_entry.save()
            return redirect('main:show_main')
        
    context = {'form': form}
    return render(request, 'create_camera_entry.html', context)

def show_xml(request):
    data = tokocamera.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')

def show_json(request):
    data = tokocamera.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

def show_xml_by_id(request, id):
    data = tokocamera.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')

def show_json_by_id(request, id):
    data = tokocamera.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    else:
        form = AuthenticationForm()
    
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_camera(request, id):
    try:
        camera = tokocamera.objects.get(pk=id)
    except tokocamera.DoesNotExist:
        raise Http404("Camera entry not found")

    form = tokocameraform(request.POST or None, instance=camera)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_camera.html", context)

def delete_camera(request, id):
    try:
        camera = tokocamera.objects.get(pk=id)
    except tokocamera.DoesNotExist:
        raise Http404("Camera entry not found")

    camera.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from .models import tokocamera

@csrf_exempt  # Exempt CSRF protection for this view (ensure you have token in your AJAX request)
@require_POST  # Ensure only POST requests are accepted
def create_tokocamera_form_ajax(request):
    try:
        # Get the data from the form submission
        name = strip_tags(request.POST.get("name"))
        price = strip_tags(request.POST.get("price"))
        description = strip_tags(request.POST.get("description"))
        user = request.user
        
        # Validate that data is not empty (optional)
        if not name or not price or not description:
            return JsonResponse({'error': 'All fields are required.'}, status=400)

        # Create the camera entry
        new_product = tokocamera(
            name=name,
            price=price,
            description=description,
            user=user
        )
        new_product.save()
        
        return JsonResponse({'message': 'Product added successfully!'}, status=201)
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

