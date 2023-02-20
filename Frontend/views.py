from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "index.html")

def header(request):
    return render(request, "page/header.html")
    
def footer(request):
    return render(request, "page/footer.html")