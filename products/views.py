from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_view(request):
    return HttpResponse('<h1>main producat page</h1>')

def choclate_view(request):
    return HttpResponse('<h1>choclate page</h1>')

def baking_view(request):
    return HttpResponse('<h1>baking ingredients page</h1>')

def decorating_view(request):
    return HttpResponse('<h1>decorating supplies page</h1>')

def pastry_view(request):
    return HttpResponse('<h1>pastry necessities page</h1>')