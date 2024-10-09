
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

1. Implement the **Registration** feature by:
```python
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib import messages
```
```python
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
```

- Create the HTML template for registration in main/templates called register.html
```html
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}

```

Route registration in urls.py in the main directory:


    from main.views import register
    ...
    urlpatterns = [
    ...
    path('register/', register, name='register'),
    ]
    ```

2. Implementing the **Login** feature by:

## Implementing the Login feature by:
```python
    from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
    from django.contrib.auth import authenticate, login
```

#### Add the login_user function:
```python
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
      if user is not None:
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response


   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

```

#### Create the HTML file for the login page in main/templates with the file name login.html
```html
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}

```

#### 3. Implementing the Logout feature by:

- Importing logout to views.py:
```python
from django.contrib.auth import logout
```

- Adding the logout_user function in the same file:
```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

```

- Adding a logout button in the main.html file in main/templates:
```html
<a href="{% url 'main:logout' %}">
    <button>Logout</button>
</a>
```

### 4.Restricting access to main page by:

- Import login_required to views.py
```python
from django.contrib.auth.decorators import login_required
```

- Add the login_required decorator above the show_main function in the same file:

```python
...
@login_required(login_url='/login')
def show_main(request):
...
```

## 5. Connecting Tokocamera and User by:

```models.py:

```

from django.contrib.auth.models import User
```

-  Adding user variable in tokocamera model
```python
   
import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class tokocamera(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField() 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   
```

- Modify the create_camera_entry function in views.py
```python
def create_camera_entry(request):
    form = tokocameraform(request.POST or None)

    if form.is_valid() and request.method == "POST":
            camera_entry = form.save(commit=False)
            camera_entry.user = request.user
            camera_entry.save()
            return redirect('main:show_main')
        
    context = {'form': form}
    return render(request, 'create_camera_entry.html', context)
```

- Modify the product_entries variable in views.py:
```python
def show_main(request):
    camera_entries = tokocamera.objects.filter(user=request.user)
```

- Run model migrations as usual
- Modify the settings.py file by importing os and changing the DEBUG variable to:
```python
import os
...
PRODUCTION = os.getenv('PRODUCTION', False)
DEBUG = not PRODUCTION
...
```

- Importing datetime, HttpResponseRedirect, and reverse to views.py

```python
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

```

- Modify the login_user function with
```python
if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
```

- Add the last_login variable in the show_main function in the same file
```js
context = {
    
    'name': request.user.username,
    'name': 'Muhammad Jordan ',
    'class': 'PBP KKI',
    'camera_entries': camera_entries,
    'last_login': request.COOKIES('last_login'),
}
```

- Modifying the logout_user function in the same file
```python
def logout_user(request):
logout(request)
response = HttpResponseRedirect(reverse('main:login'))
response.delete_cookie('last_login')
return response

```
```sh
    python manage.py runserver
```

## Assignment 5

##### 1. If there are multiple CSS selectors for an HTML element, explain the priority order of these CSS selectors!


Inline styles (e.g., style="...") have the highest priority.
IDs (e.g., #id) have higher priority than classes, attributes, and pseudo-classes.
Classes, attributes, and pseudo-classes (e.g., .class, [attribute], :hover) have higher priority than elements and pseudo-elements.
Elements and pseudo-elements (e.g., div, :before) have the lowest priority.

#### 2. Why does responsive design become an important concept in web application development? Give examples of applications that have and have not implemented responsive design!


Importance of Responsive Design:
Improved User Experience: Users can easily navigate and interact with the site regardless of the device they are using.

Example of applicaiton:
Airbnb: The site adapts to different screen sizes, ensuring a smooth booking experience on any device

#### 3. Explain the differences between margin, border, and padding, and how to implement these three things!


### 1.Margin:

- Definition: The space outside the border of an element.
- Purpose: Creates space between the element and other elements around it.
- Implementation: margin property in CSS

### 2.Border:

- Definition: The line that surrounds the padding and content of an element.
- Purpose: Defines the boundary of an element and can be styled with different colors, widths, and styles.
- Implementation: border property in CSS.

### 3.Padding:

- Definition: The space between the content of an element and its border.
- Purpose: Creates space inside the element, around the content.
- Implementation: padding property in CSS.
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Margin, Border, and Padding Example</title>
  <style>
    .example {
      margin: 20px; /* Space outside the border */
      border: 2px solid black; /* Border around the element */
      padding: 10px; /* Space inside the border */
      background-color: lightblue; /* Background color for visibility */
    }
  </style>
</head>
<body>
  <div class="example">
    This is an example element.
  </div>
</body>
</html>
```

### 4. Explain the concepts of flex box and grid layout along with their uses!


### Flexbox
Concept:

- Flexbox, or the Flexible Box Layout, is a CSS layout model designed to provide a more efficient way to lay out, align, and distribute space among items in a container, even when their size is unknown or dynamic.
Uses:

- One-dimensional layout: Flexbox is ideal for laying out items in a single direction (either as a row or a column).
Alignment: Easily align items along the main axis (horizontal or vertical) and the cross axis.
Space distribution: Distribute space between items or around items.
Responsive design: Adjust the layout of items based on the available space.

### Grid Layout
Concept:

- The CSS Grid Layout is a two-dimensional layout system for the web. It allows developers to create complex layouts on the web more easily and consistently across browsers.
Uses:

- Two-dimensional layout: Grid is ideal for creating layouts that require both rows and columns.
Explicit placement: Precisely place items into a grid defined by rows and columns.
Complex layouts: Create complex and responsive layouts with ease.
Example:


## Assigment 6

## Benefits of Using JavaScript in Developing Web Applications
Interactivity: JavaScript allows developers to create highly interactive user interfaces, enhancing user experience.

Client-Side Processing: Reduces server load by handling tasks on the client side, leading to faster response times.


## Why Use await with fetch()
Purpose: await is used to pause the execution of an async function until the fetch() promise is resolved.

Without await: The function would continue executing the subsequent lines of code before the fetch() call completes, leading to potential errors or undefined behavior.

### Need for csrf_exempt Decorator on AJAX POST View
CSRF Protection: Django includes Cross-Site Request Forgery (CSRF) protection by default.

AJAX Requests: AJAX POST requests might not include the CSRF token, causing the request to be blocked.

Decorator Usage: csrf_exempt disables CSRF protection for that specific view, allowing the AJAX request to succeed.

Back-End User Input Sanitization
Security: Front-end sanitization can be bypassed by malicious users, making back-end sanitization crucial.

Consistency: Ensures that all data entering the system is sanitized, regardless of the source.

By sanitizing input on the back-end, you ensure a consistent and secure approach to handling user data.

