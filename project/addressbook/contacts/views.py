from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Contact

# Create your views here.
def contacts(request):
    mycontacts = Contact.objects.all().values()
    template = loader.get_template('all_contacts.html')
    context = {
        'mycontacts': mycontacts,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mycontact = Contact.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mycontact': mycontact,
    }
    return HttpResponse(template.render(context, request))

def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry', 'Pineapple', 'Orange'],   
    }
    return HttpResponse(template.render(context, request))