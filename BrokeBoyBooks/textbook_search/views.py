from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'textbook_search/index.html')

def addTextbook(request):
    return render(request, 'textbook_search/addTextbook.html')

def displayTextbook(request):
    return render(request, 'textbook_search/displayTextbook.html')