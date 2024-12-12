from django.shortcuts import render
from django.http import HttpResponse

#   1 -> app/urls.py
def index(request): 
    context = {
        'title' : 'Home - Main',
        'content' : 'Furniture shop'
    }
    return render(request, 'main/index.html', context)    

def about(request): 
    context = {
        'title' : 'Page - ABOUT',
        'content' : "About us",
        'text_on_page' : "Some text over ther"
    }
    return render(request, 'main/about.html', context)