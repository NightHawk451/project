import random

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from django.views import View


# Create your views here.

# class HomePageView(TemplateView):
# 	def get(self, request, **kwargs):
# 		context = {}
# 		return render(request, 'index.html', context)






class HomeView(TemplateView):
    template_name ='home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args,**kwargs)
        num = None
        num = random.randint(0, 100000000)
        some_list = [num, random.randint(0, 100000000), random.randint(0, 100000000), random.randint(0, 100000000) ]
        context = {"html_var": True, 
                "num": num,
                "some_list":some_list
                }
        print(context)
        return context

# class AboutView(TemplateView):
#     template_name ='contact.html'


# class ContactTemplateView(TemplateView):
#     template_name ='contact.html'



# def home(request):
#     num = random.randint(0, 100000000)
#     some_list = [num, random.randint(0, 100000000), random.randint(0, 100000000), random.randint(0, 100000000) ]
#     context = {"html_var": True, 
#                 "num": num,
#                 "some_list":some_list
#                 }
#     return render(request, "home.html", context)

# def about(request):
#     context = {}
#     return render(request, "about.html", context)

# def contact(request):
#     context = {}
#     return render(request, "contact.html", context)

# class ContactViewOld(View):
#     def get(self, request, *args, **kwargs):
#         context = {}
#        # print(kwargs)
#         return render(request, "contact.html", context)