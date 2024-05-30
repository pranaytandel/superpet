from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout

def home (request):
    return render(request,'index.html')


def register(request):
    message=None
    if request.method=="GET":
        #form=UserCreationForm()
        form=CustomUserCreationForm()
    if request.method=="POST":
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            message="User registration successfull"
        else:
            message="User registration failed..."
    return render(request,"register.html",{"form":form,"message":message})

#===============================================================================
#login
def user_login(request):
    if request.method=="GET":
        return render(request,'login.html')
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return HttpResponseRedirect("/products")
        else:
            return render(request, 'login.html', {"error_message": "Invalid credentials. Please try again."})

#=======================================================
#logout

def user_logout(request):
     logout(request)
     return HttpResponseRedirect("/login")

#----------------------------------------------------------
# Template filter examples

def template_filter_example(request):
    data="Hello I am Learning template filter"
    return render(request,"demo.html",{"data":data})
    


