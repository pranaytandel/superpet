from django.shortcuts import render,HttpResponse
from django.views import View

# Create your views here.
def home (request):
    return HttpResponse("<h1>this is first view </h1>")

def index(request):
    return HttpResponse("<h1> Home page </h1>")

def contact(requrst):
    return HttpResponse("<h1> Pranay tandel</h1>")

def aboutus(reqest):
    return HttpResponse("<h1> veer bhai </h1>")

def comment(request):
    return render(request,"comment.html",{"name":"pranay","age":24})

def subject(request):
    subjects=["marathi","hindi","english","maths"]
    return render(request,"subject.html",{"subjects":subjects})

def inputData(request):
    if request.method=="GET":
        username=request.GET.get("username","")
        #city=request.GET.get("city","")
        return render(request,"input.html",{"username":username})   
        
    
    elif request.method=="POST":
        username=request.POST.get("username")
        city=request.POST.get("city","")
        return render(request,"input.html",{"username":username,"city":city})
    
    #class based  views
class Book(View):
        def get (self,request):
            return render(request,"book.html")

        def post (self,request):
            bookname=request.POST.get("bookname")
            bookprice=request.POST.get("bookprice")
            return render(request,"book.html",{"bookname":bookname,"bookprice":bookprice})
    


    








