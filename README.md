# Toko camera


## Assignment 2 

### 1. Steps: 
1. Make a new local directory named ```tugas1```
2. Initialized as well configuring ```git``` in the repository
3. Create a new repository in GitHub with the same name
4. Connecting local repository with the GitHub repository by:
   - Setting a new branch named ```main``` using:

    ```bash
    git branch -M main
    ```
   - Connecting the local repository to GitHub using:

    ```bash
    git remote add origin https://github.com/jordanaziz18/tugas1
    ```
5. In the local directory, set up a virtual environment by running:

    ```bash
    python -m venv env
    ```
   And activating it by:

    ```bash
    env\Scripts\activate
    ```
6. Set up requirements in the same local directory by:
   - Creating a new directory called ```requirements.txt``` with the contents being: 

    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
   - Running the command to enable the requirements

   ```bash
   pip install -r requirements.txt
   ```
7. Create a new Django project by running:
    ```bash
    django-admin startproject tugas1 .
    ```
8. Add the following to ```ALLOWED_HOST``` to allow access to local host:
    
    ```
    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
    ```
9. Create the ```main``` app inside the main directory by:
    - Running the following command

    ```bash
    python manage.py startapp main
    ```
    - And adding ```main``` to the ```INSTALLED_APPS``` in ```settings.py```

    ```
    INSTALLED_APPS = [
    'main'
    ]
    ```
10. Create a new directory in ```main``` named ```templates``` with a ```html``` file named ```main.html``` with the contents:

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UnlimitedBacon</title>
    </head>
    <body>
        <h1>
            {{ app_name }}
        </h1>

        <p>
            {{ name }}
        </p>
        <p>
            {{ class }}
        </p>
    </body>
    </html>
    ```
11. Adding new models by modifying ```models.py``` by:
    - Adding the following to the file:

    ```python
    from django.db import models

    class tugas1 (models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    stock = models.IntegerField()
    ```
    - Execute the two commands to migrate any changes made to the ```model.py``` file:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
12. Integrating the ```views.py``` file with the ```main.html``` file:
    
    ```python
    from django.shortcuts import render

    def show_main(request):
        context = {
            'app_name': 'Toko camera',
            'name': 'Muhammad Jordan Ar-Razi Aziz',
            'class': 'KKI'
        }

        return render(request, 'main.html', context)
    ```
13. Route the ```main``` application to the ```urls.py``` file by:
    - Adding the following to ```urls.py``` in the ```main``` directory

    ```python
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
    - Add a URL route in the ```urls.py``` file in the ```tugas1 directory by:
    
    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')),
    ]
    ```
14. Test the app by:
    - Running the application by running the command:
    
    ```bash
    python manage.py runserver
    ```
    - Then open 
    
    ```bash
    http://localhost:8000/
    ```



### 2. Use of ```git```
Git is an essential tool in software development for several key reasons:

Version Control: Git enables developers to track changes made to the codebase and revert to previous versions if necessary.
Collaboration: With git, multiple developers can work on the same project concurrently using branches. Each developer can create their own branch, allowing them to work independently without impacting the main codebase. Additionally, git supports pull requests, which facilitate team discussions and reviews before changes are merged into the primary project.

### 3. Reason to use Django
Django is frequently selected as an entry point for learning software development due to its comprehensive framework that streamlines the development process through numerous built-in features. It boasts extensive, beginner-friendly documentation and employs the Model-View-Template (MVT) architecture, which aids newcomers in understanding fundamental web development principles. Django prioritizes security, has a robust community, and is utilized in many professional applications.

### 4. ORM
The Django model is called an **ORM** (Object-Relational Mapping) because it allows developers to interact with a database using Python classes instead of raw SQL. It maps Python objects to database tables, automatically handling the translation between the two.
