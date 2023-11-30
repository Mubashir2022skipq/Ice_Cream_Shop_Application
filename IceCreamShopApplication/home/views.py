from django.shortcuts import render , HttpResponse
from home.models import Contact
from datetime import datetime 
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable" : "this is sent"
        
        }
    
    return render(request,'index.html',context)
    # return HttpResponse("this is home page")

def about(request):
    return render(request,'about.html')
    

def services(request):
    return render(request,'services.html')
    

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        des = request.POST.get('des')
        contact = Contact(name=name, email=email, phone=phone, des=des, date=datetime.today())
        contact.save()
        messages.success(request, "Your message Has been sent !")

    return render(request,'contact.html')
    