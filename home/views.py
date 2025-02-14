from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

def index(request):
    if request.method == 'POST': 
        form = ContactForm(request.POST)
        if form.is_valid(): # if data are correct gohead
            form.save()
            form = ContactForm() #after the process make new empty form
    else:
        form = ContactForm()
    
    context = {
        'form' : form
    }
    
    return render(request, 'home/index.html', context)


def contact(request):
    
    if request.method == 'POST': 
        form = ContactForm(request.POST)
        if form.is_valid(): # if data are correct gohead
            form.save()
            form = ContactForm() #after the process make new empty form
    else:
        form = ContactForm()
    
    context = {
        'form' : form
    }
    
    return render(request, "home/contact.html", context)