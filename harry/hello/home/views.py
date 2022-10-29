from multiprocessing import context
# import re
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable" : "i am variable m",
        "ref" :"manish"
    }
    return render(request,'index.html', context) 

def about(request):
    return render(request,'about.html') 

    # return HttpResponse(" This is abou tpage!") 

def services(request):
    return render(request,'services.html') 

    # return HttpResponse(" This is service page!") 
    
def contacts(request):
    return render(request,'contacts.html') 

    # return HttpResponse(" this is my contact details")

# def home(request):
#     return render(request,'home.html') 
