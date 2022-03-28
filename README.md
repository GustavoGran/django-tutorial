# django-tutorial

## Understanding views and url paths

First let's start by installing django in a virutal environment of your repository
```shell
python3 -m venv venv
source venv/bin/activate
pip install django
```

Now let's start a project
```shell
django-admin startproject mysite
```

Let's run our project into a localserver: change into mysite directory and run manage.py
```shell
cd mysite
# Specify a port after run server if you wan anything diffrent than 8000
python manage.py runserver
```
Let's create an application in our project
```shell
python manage.py startapp myapp
```

Go into myapp directory and into views.py file. A view of an application is a web page that will be presented to user, serving the http response.

Add the http response and add some functions to add views
```python
from django.http import HttpResponse

def index(response):
    return HttpResponse("<h1>Tutorial</h1>")
```

Now we need to configure the `urls.py` file to redirect path to the view you've just created. if i doesn't exist yet, create it
```python
touch myapp/urls.py

# inside urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```
We need also to set the url path to the application itself, since a project can have many apps. To do so, let's use the `urls.py` file in the mysite **sub**directory

```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("myapp.urls")),
]
```

## Databases

The basic and default database for using django is a in-file database sqlite3. It can be really useful for test purposes and local projects.

To understand the handling of databases in django we should probably first understand migration, ORM and what it means.

### Migrations
If you have ever worked with databses in your life you will probably know how difficult it is to manage change in database schemas. Performing "migrations" in database schema is complex and may require some backups and lot of attention.

Django handles database schema change through a version control system called migrations. The frameworok determines the required changes based on changes to the object models (ORM).

### ORM
Object Relational Model is a way of handling database objects as OOP objects and therefore simplify CRUD operations in databases. Django is an ORM enabled framework, which means that you don't need to directly declare databse schemas, they are infered from object models.

### Plug-in apps and applying migrations

Since Django is a framework with a app plug-in philosophy, you need to tell django which apps are installed and which are not. To do so, you'll need to access your `settings.py` file in the project directory and modify `INSTALLED_APPS` list to include the Config class of your app in `myapp/apps.py`.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp.apps.MyappConfig',
]
```

After that you should be able to migrate. `makemigrations` is like adding changes to the stagin area in git with `git add .`, while `migrate` apply those changes to the project like `git commit`.

```
python manage.py makemigrations myapp
python manage.py migrate
```

### Models
Objects that define data and database schemas. Reach to the `models.py` file in your app directory and create some classes with CamelCase notation. You can use models.ForeignKey to determine relations between objects.

```python
from django.db import models

# Create your models here.
class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    # print method
    def __str__(self):
        return self.name

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)    
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
```

Make sure to run `makemigrations` and `migrate` after modifying the model schema

### Adding data to the database

To add some data manually into the database access python shell
```shell
python manage.py shell
Python 3.8.10 (default, Nov 26 2021, 20:14:08) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from myapp.models import Item, ToDoList
>>> t = ToDoList(name="Gran\'s List")
>>> t.save()
>>> ToDoList.objects.all()
<QuerySet [<ToDoList: Gran's List>]>
>>> 
>>> ToDoList.objects.get(id=1)
<ToDoList: Gran's List>
>>> 
```
