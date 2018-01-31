import random

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

# class HomePageView(TemplateView):
# 	def get(self, request, **kwargs):
# 		context = {}
# 		return render(request, 'index.html', context)

def home(request):
    num = random.randint(0, 100000000)
    some_list = [num, random.randint(0, 100000000), random.randint(0, 100000000), random.randint(0, 100000000) ]
    context = {"html_var": True, 
                "num": num,
                "some_list":some_list
                }
    return render(request, "home.html", context)

def about(request):
    context = {}
    return render(request, "about.html", context)

def contact(request):
    context = {}
    return render(request, "contact.html", context)


