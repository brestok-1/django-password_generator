from django.shortcuts import render
from django.http import HttpResponse
from random import *
import string


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    chars = string.ascii_lowercase
    if request.GET.get('uppercase'):
        chars += string.ascii_uppercase
    if request.GET.get('numbers'):
        chars += string.digits
    if request.GET.get('special'):
        chars += '?<>/.\\)(^%#@$+-_*'
    length = int(request.GET.get('length', 12))
    thepassword = ''.join(sample(chars, length))
    return render(request, 'generator/password.html', {'password': thepassword})


def info(request):
    return render(request, 'generator/information.html')
