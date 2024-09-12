from django.shortcuts import render
from django.http import HttpResponse
from Landingpage.models import Contact

# Create your views here.
def home(reqeust):
    return render(reqeust,'home.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']


        # print(name,email,phone,desc)
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        print("data has been retain to the db")

    return render(request,'contact.html')



