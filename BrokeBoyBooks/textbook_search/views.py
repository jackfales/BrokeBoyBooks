from django.shortcuts import render
from django.http import HttpResponse

from .forms import AddTextbookForm

# Create your views here.

def index(request):
    return render(request, 'textbook_search/index.html')

def addTextbook(request):
    if request.method == 'POST':
        form = AddTextbookForm()
        if form.is_valid():
            form.save()
        else:
            print("form not valid")
    else:
        form = AddTextbookForm()
    return render(request, 'textbook_search/addTextbook.html', {'form' : form})

def displayTextbook(request):
    return render(request, 'textbook_search/displayTextbook.html')