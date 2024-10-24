from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def wish1(request):
    return HttpResponse("Happy Sanskranthi")
def wish2(request):
    return HttpResponse("Happy Ramadan")
def wish3(request):
    return HttpResponse("Happy Ugadi")