#Imports
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect

# Methods
def index(request):
    context = {
    }
    return render(request, 'home/index.html', context)