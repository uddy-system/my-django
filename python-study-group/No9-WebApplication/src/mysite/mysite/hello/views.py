from django.shortcuts import render
from django.http.response import HttpResponse

def hello_world(request):
    return HttpResponse('<H1>こんにちは！</H1>')
