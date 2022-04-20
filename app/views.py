# from turtle import onclick
# from unittest import result
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def services(request):
     render(request, 'services.html')
def news(request):
    return render(request, 'news.html')
def contact(request):
    return render(request, 'contact.html')