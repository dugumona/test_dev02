from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#MTV  --V view文件

def say_hello(request):
    #print("say_hello")
    name = request.GET.get("name", "")
    return HttpResponse(f"hello {name}")