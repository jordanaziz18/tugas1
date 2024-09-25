
# Toko camera


## Assignment 2 

### 1. Steps: 
```tugas1```
2. Initialized as well configuring ```git``` in the repository
3. Create a new repository in GitHub with the same name
4. Connecting local repository with the GitHub repository by:
   - Setting a new branch named ```main``` using:

```

    git branch -M main
    ```
   - Connecting the local repository to GitHub using:

```sh
    git remote add origin https://github.com/jordanaziz18/tugas1
```

5. In the local directory, set up a virtual environment by running:

```sh
    python -m venv env
```

   And activating it by:

```sh
    env\Scripts\activate
```

6. Set up requirements in the same local directory by:
```requirements.txt```

```

    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
   - Running the command to enable the requirements

```sh
   pip install -r requirements.txt
```

7. Create a new Django project by running:
```sh
    django-admin startproject tugas1 .
```
```ALLOWED_HOST```
    
```

    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
    ```
```main```
    - Running the following command

```

    python manage.py startapp main
    ```
```main```

```

    INSTALLED_APPS = [
    'main'
    ]
    ```
```main```

```

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
```models.py```
    - Adding the following to the file:

```

    from django.db import models

    class tugas1 (models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    stock = models.IntegerField()
    ```
```model.py```

```

    python manage.py makemigrations
    python manage.py migrate
    ```
```views.py```
    
```

    from django.shortcuts import render

    def show_main(request):
        context = {
            'app_name': 'Toko camera',
            'name': 'Muhammad Jordan Ar-Razi Aziz',
            'class': 'KKI'
        }

        return render(request, 'main.html', context)
    ```
```main```
    - Adding the following to ```urls.py``` in the ```main``` directory

```

    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
```urls.py```
    
```

    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')),
    ]
    ```
14. Test the app by:
    - Running the application by running the command:
    
```sh
    python manage.py runserver
```

    - Then open 
    
```sh
    http://localhost:8000/
```
```git```
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

```

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

```base.html```
    - Opening ```settings.py``` and adjust the code:
    
```

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates'], # FILLING THE LIST WITH THIS CONTENT
            ...
        }
    ```

3. Changing IDs of models using UUID by:
```uuid```

```

    import uuid 
    from django.db import models
    ```
```id```

```

    # Create your models here.
    class tokocamera(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
        name = models.CharField(max_length=100)
        price = models.IntegerField()
        description = models.TextField()
        stock = models.IntegerField()    
    ```
```models.py```

4. Create ```forms.py``` in the ```main``` directory, and fill it in with the following contents:

```

    from main.models import tokocamera
    from django import forms

    class tokocameraForm(forms.ModelForm):
        class Meta:
            model = tokocamera
            fields = '__all__'
    ```
```views.py```
    - Importing ```redirect``` from ```django.shortcuts```:

```

    from django.shortcuts import render, redirect
    ```
```create_camera_entry```

```

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
```show_main```

```

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

```urls.py```
    - Importing the recently created ```create_camera_entry``` function

```

    from main.views import show_main, create_mood_entry
    ```
```url_patterns```

```

    urlpatterns = [
        path('', show_main, name='show_main'),
        path('create_camera_entry', create_camera_entry, name='create_camera_entry'),
    ]
    ```

```main/templates```
    - Creating a new HTML file named ```create_camera_entry.html``` with the following contents:

```

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
```main.html```

```

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

    urlpatterns = [
        ...
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'),
        path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    ]
    ```

9. Last but not least, testing the site in the localhost with

```sh
    python manage.py runserver
```

## Assignment 4

### 1. What is the difference between HttpResponseRedirect() and redirect()

#### HttpResponseRedirect(): 
1. It is a class-based response.
2. You need to provide the full URL as an argument.
```sh
from django.http import HttpResponseRedirect
response = HttpResponseRedirect(reverse("main:show_main"))
```

### redirect()
- It is a shortcut function provided by Django.
- It can take a URL, a view name, or a view name with arguments.
- It is more flexible and easier to use.

```sh
from django.shortcuts import redirect

  if form.is_valid() and request.method == "POST":
            camera_entry = form.save(commit=False)
            camera_entry.user = request.user
            camera_entry.save()
            return redirect('main:show_main')
```

## 2. MoodEntry link with User

The MoodEntry model can be linked to the built-in User model using a foreign key. This relationship allows each mood entry to be associated with a specific user, enabling personalized data management.

## 3. Authentication vs Authorization

### Authentication:
- Definition: The process of verifying the identity of a user or system.
- Purpose: Ensures that the entity is who it claims to be.
### Authorization:
- Definition: The process of determining what an authenticated user or system is allowed to do.
- Purpose: Controls access to resources and actions based on permissions.

- summary:
In summary, authentication verifies identity, while authorization grants access based on that identity.

## 4. Use of Cookies

### How Django Remembers Logged-In Users
- Django uses cookies to remember logged-in users. When a user logs in, Django creates a session and stores the session ID in a cookie on the user's browser. This session ID is then used to identify the user in subsequent requests.

### Are All Cookies Safe to Use?
Not all cookies are inherently safe. Here are some considerations:
- Secure Cookies: Should be used to store sensitive information and should only be transmitted over HTTPS.
- HttpOnly Cookies: Cannot be accessed via JavaScript, reducing the risk of XSS attacks.

## Summary
- Django uses cookies to manage user sessions and remember logged-in users. While cookies have various uses, their safety depends on how they are implemented and secured. Proper use of secure, HttpOnly, and SameSite attributes can enhance cookie security.


## 5. Steps
