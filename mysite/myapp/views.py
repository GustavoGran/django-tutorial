from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import ToDoList, Item

# Create your views here.

def index(request, id):
    tdls = ToDoList.objects.get(id=id)
    return render(request, "myapp/list.html",{"tdls":tdls})

def home(request):
    return render(request, "myapp/home.html",{})