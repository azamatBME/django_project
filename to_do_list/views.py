from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'to_do_list/home.html')

def about(request):
    return render(request, 'to_do_list/about.html')

