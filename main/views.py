from django.shortcuts import render
from django.http import HttpResponse

#   1 -> app/urls.py
def index(request): 
    context = {
        'title' : 'Home',
        'content' : 'Main shop page - HOME', 
        'list' : ['first', 'second'],
        'dict' : {'first' : 1}, 
        'bool' : True
    }
    return render(request, 'main/index.html', context)    

def about(request): 
    return HttpResponse("About")