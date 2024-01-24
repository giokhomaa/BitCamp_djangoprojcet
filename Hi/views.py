from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request, name):
#     return HttpResponse(f'hello {name}')

def index(request, name):
    return render(request, "Hi/index.html", {
        #იქმნება ცვლადი, რომელსაც გამოვიყენებ html-ში
        "name":name
    })


