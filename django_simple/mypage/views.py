from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello all, it's my first page.")