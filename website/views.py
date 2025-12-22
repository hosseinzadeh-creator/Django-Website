from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_view(request):
    return HttpResponse('<h1>Home Page</h1>')
def aboutus_view(request):
    return HttpResponse('<h1>aboutUS page</h1>')

def contactus_view(request):
    return HttpResponse('<h1>contactUS page </h1>')