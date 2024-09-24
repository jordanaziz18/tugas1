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
    <title>tokocamera</title>
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


## Assignment 3

### 1. Data Delivery Purpose
Data delivery is crucial in implementing a platform for several reasons:

Real-Time Access: Efficient data delivery ensures that users have real-time access to the information they need, enhancing user experience and engagement.

Data Integrity: Reliable data delivery mechanisms maintain the integrity of the data being transferred, ensuring that users receive accurate and consistent information.



### 2. XML v JSON
XML is more suitable for complex documents with rich structures and metadata, while JSON is preferred for lightweight data interchange, especially in web applications. The choice between the two often depends on the specific requirements of the application and the data being handled.

### 3. Usage of ```is_valid()```
Importance of is_valid()
Data Integrity: Ensures that only valid data is processed and stored, maintaining the integrity of the application.
User Experience: Provides immediate feedback to users about what went wrong with their input, enhancing the overall user experience.


### 4. Purpose of the ```csfr_token```
The csrf_token is crucial for protecting against Cross-Site Request Forgery (CSRF) attacks in web applications, including those built with Django. Here’s why it's necessary and the potential consequences of not using it:
 Protection Against CSRF Attacks: CSRF is an attack that tricks a user into submitting a request to a web application in which they are authenticated, without their consent.
 
Consequences of Not Using csrf_token
Vulnerability: Without the CSRF token, a malicious site could forge requests on behalf of an authenticated user, leading to unauthorized actions such as changing user settings, making purchases, or even deleting accounts.
Data Integrity Risks: Sensitive operations could be executed without the user's knowledge, compromising data integrity and security.

### 5. Steps:
1. Creating Base HTML template by:
   - Creating ```templates``` directory in the ```Root``` directory
   - Create ```base.html``` file with the contents:

   ```html
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        {% block meta %} {% endblock meta %}
    </head>

    <body>
        {% block content %} {% endblock content %}
    </body>
    </html>
    ```

2. Make ```base.html``` as a template file by:
    - Opening ```settings.py``` and adjust the code:
    
    ```python
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates'], # FILLING THE LIST WITH THIS CONTENT
            ...
        }
    ```

3. Changing IDs of models using UUID by:
    - Importing the ```uuid``` library

    ```python
    import uuid 
    from django.db import models
    ```
    - Adding the ```id``` model in ```models.py```:

    ```python
    # Create your models here.
    class tokocamera(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
        name = models.CharField(max_length=100)
        price = models.IntegerField()
        description = models.TextField()
        stock = models.IntegerField()    
    ```
    - Then migrate any changes in ```models.py``` as usual

4. Create ```forms.py``` in the ```main``` directory, and fill it in with the following contents:

    ```python
    from main.models import tokocamera
    from django import forms

    class tokocameraForm(forms.ModelForm):
        class Meta:
            model = tokocamera
            fields = '__all__'
    ```
5. Update the ```views.py``` file by:
    - Importing ```redirect``` from ```django.shortcuts```:

    ```python
    from django.shortcuts import render, redirect
    ```
    - Adding the ```create_camera_entry``` function:

    ```python
    def create_camera_entry(request):
        form = tokocameraForm()

        if request.method == 'POST':
            form = tokocameraForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('main:show_main')
            
        context = {'form': form}
        return render(request, 'create_camera_entry.html', context)
    ```
    - Updating the ```show_main``` function:

    ```python
    def show_main(request):
        product_entries = tokocamera.objects.all() # ADDED product_entries VARIABLE

        context = {
            'app_name' : 'Unlimited camera',
            'name': 'Muhammad Ghaza Fadhlilbaqi',
            'class': 'PBP KKI',
            'product_entries': product_entries, # ADDED product_entries VARIABLE... again...
        }

        return render(request, "main.html", context)
    ```

6. Updating ```urls.py``` in the ```main``` directory by:
    - Importing the recently created ```create_camera_entry``` function

    ```python
    from main.views import show_main, create_mood_entry
    ```
    - Adding a new URL path to ```url_patterns``` list

    ```python
    urlpatterns = [
        path('', show_main, name='show_main'),
        path('create_camera_entry', create_camera_entry, name='create_camera_entry'),
    ]
    ```

7. Creating and modifying HTML files in ```main/templates``` by:
    - Creating a new HTML file named ```create_camera_entry.html``` with the following contents:

    ```html
    {% extends 'base.html' %} 
    {% block content %}
    <h1>Add New Product Entry</h1>

    <form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
        <td></td>
        <td>
            <input type="submit" value="Add Product" />
        </td>
        </tr>
    </table>
    </form>

    {% endblock %}
    ```
    - Modifying the ```main.html``` file into:

    ```html
    {% extends 'base.html' %}
    {% block content %}
    <h1>{{ app_name }}</h1>

    <h5>Name:</h5>
    <p>{{ name }}</p>

    <h5>Class:</h5>
    <p>{{ class }}</p>


    {% if not product_entries %}
    <p>There are no products available in the shop.</p>
    {% else %}
    <table>
    <tr>
        <th>Product Name</th>
        <th>Price</th>
        <th>Description</th>
        <th>Stock</th>
    </tr>

    {% for product_entry in product_entries %}
    <tr>
        <td>{{product_entry.name}}</td>
        <td>{{product_entry.price}}</td>
        <td>{{product_entry.description}}</td>
        <td>{{product_entry.stock }}</td>
    </tr>
    {% endfor %}
    </table>
    {% endif %}

    <br />

    <a href="{% url 'main:create_camera_entry' %}">
    <button>Add Product</button>
    </a>

    {% endblock content %}
    ```

8. Creating Functions for XML, JSON, XML by ID and JSON by ID:
    - the XML function

    ```python
    def show_xml(request):
        data = tokocamera.objects.all()
        return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')
    ```
    
    - the JSON function

    ```python
    def show_json(request):
        data = tokocamera.objects.all()
        return HttpResponse(serializers.serialize('json', data), content_type='application/json')
    ```

    - the XML by ID function

    ```python
    def show_xml_by_id(request, id):
        data = tokocamera.objects.filter(pk=id)
        return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')
    ```

    - the JSON by ID function

    ```python
    def show_json_by_id(request, id):
        data = tokocamera.objects.filter(pk=id)
        return HttpResponse(serializers.serialize('json', data), content_type='application/json')
    ```

9. Routing the 4 new functions the ```urls.py``` file in the ```main``` directory

    ```python
    urlpatterns = [
        ...
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'),
        path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    ]
    ```

10. Last but not least, testing the site in the localhost with

    ```bash
    python manage.py runserver
    ```



