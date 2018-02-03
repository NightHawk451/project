import random

from django.shortcuts import render
from django.contrib.auth import get_user_model, login , logout
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView

from django.views import View

from .forms import UserCreationForm, UserLoginForm

User = get_user_model()

# Create your views here.

# class HomePageView(TemplateView):
# 	def get(self, request, **kwargs):
# 		context = {}
# 		return render(request, 'index.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/login")

def login_view(request, *args, **kwargs):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        user_obj = form.cleaned_data.get('user_obj')
        login(request, user_obj)
        return HttpResponseRedirect("/")
    return render(request, "registration/login.html", {"form": form})

# def login_view(request,*args,**kwargs):
#     form = UserLoginForm(request.POST or None)
#     if form.is_valid():
#         user_obj = form.cleaned_data.get('user_obj')
#         #user_obj =  User.objects.get(username__iexact=query)
#         login(request, user_obj) # logging in part, validation is done on UserLoginForm
#         return HttpResponseRedirect("/")
#     return render(request, "registration/login.html", {"form": form})


def register(request, *args, **kwargs):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/login")
    return render(request, "registration/register.html", {"form": form})



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