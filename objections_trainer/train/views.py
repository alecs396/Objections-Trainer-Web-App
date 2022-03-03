from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Trainer</h1>')

def add_objection(request):
    return HttpResponse('<h1>Create New Objection</h1>')