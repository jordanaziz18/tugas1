#!/bin/bash
echo '!!output-start-cell'
cd c:\Users\Jordan\Desktop\Kuliah\Class\SEM 3\PBP\assigment\tugas1
    git remote add origin https://github.com/jordanaziz18/tugas1#!/bin/bash
echo '!!output-start-cell'
cd c:\Users\Jordan\Desktop\Kuliah\Class\SEM 3\PBP\assigment\tugas1
    python -m venv env#!/bin/bash
echo '!!output-start-cell'
cd c:\Users\Jordan\Desktop\Kuliah\Class\SEM 3\PBP\assigment\tugas1
    env\Scripts\activate#!/bin/bash
echo '!!output-start-cell'
cd c:\Users\Jordan\Desktop\Kuliah\Class\SEM 3\PBP\assigment\tugas1
   pip install -r requirements.txt#!/bin/bash
echo '!!output-start-cell'
cd c:\Users\Jordan\Desktop\Kuliah\Class\SEM 3\PBP\assigment\tugas1
    django-admin startproject tugas1 .#!/bin/bash
echo '!!output-start-cell'
cd c:\Users\Jordan\Desktop\Kuliah\Class\SEM 3\PBP\assigment\tugas1
    python manage.py runserver#!/bin/bash
echo '!!output-start-cell'
cd c:\Users\Jordan\Desktop\Kuliah\Class\SEM 3\PBP\assigment\tugas1
    http://localhost:8000/#!/bin/bash
echo '!!output-start-cell'
cd c:\Users\Jordan\Desktop\Kuliah\Class\SEM 3\PBP\assigment\tugas1
    python manage.py runserver#!/bin/bash
echo '!!output-start-cell'
cd c:\Users\Jordan\Desktop\Kuliah\Class\SEM 3\PBP\assigment\tugas1
from django.http import HttpResponseRedirect
response = HttpResponseRedirect(reverse("main:show_main"))#!/bin/bash
echo '!!output-start-cell'
cd c:\Users\Jordan\Desktop\Kuliah\Class\SEM 3\PBP\assigment\tugas1
from django.shortcuts import redirect

  if form.is_valid() and request.method == "POST":
            camera_entry = form.save(commit=False)
            camera_entry.user = request.user
            camera_entry.save()
            return redirect('main:show_main')