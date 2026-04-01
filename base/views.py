from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.

def home(req):
    return render(req,'home.html')

