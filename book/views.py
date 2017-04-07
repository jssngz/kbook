from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import  HttpResponseRedirect
from django.shortcuts import render
from django.urls import  reverse
def  index(request):
    return HttpResponse("welcome")
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse('result:'+str(c))
def add2(request,a,b):
    c = int(a)+int(b)
    return HttpResponse('result:'+str(c))
def home(request):
    return render(request,'home.html')

def old_add2_redirect(request,a,b):
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
    )

