from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import ContactForm ,LoginForm, RegisterForm

def home_page(request):
    #print(request.session.get("first_name","Unknown"))
    contactform=ContactForm(request.POST or None)
    context={
    "title":"about page",
    "data":"no data",
    "form":contactform
    }
    if request.user.is_authenticated:
        context["premium"]="noooooooooooo"
    if contactform.is_valid():
        print(contactform.cleaned_data)
    # if request.method == "POST":
    #     print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request,"home.html",context)

def login_page(request):

      form=LoginForm(request.POST or None)
      context={
       "form" :form
      }
      print("user logged in")
     # print(request.user.is_authenticated)
      if form.is_valid():

          print(form.cleaned_data)
          username=form.cleaned_data.get('username')
          password=form.cleaned_data.get('password')
          user=authenticate(request,username=username,password=password)
          #print(request.user.is_authenticated)
          if user is not None:
              print(request.user.is_authenticated)
              login(request,user)
              return redirect("/login")

          else:
              print("error")
      return render(request,"auth/login.html",context)

user=get_user_model()
def register_page(request):

       form=RegisterForm(request.POST or None)
       context={
        "form" :form
       }
       print("user logged in")
      # print(request.user.is_authenticated)
       if form.is_valid():
           print(form.cleaned_data)
           username=form.cleaned_data.get('username')
           password=form.cleaned_data.get('password')
           email=form.cleaned_data.get('email')
           new_user=user.objects.create_user(username,email,password)
           print(new_user)

       return render(request,"auth/register.html",context)
