from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.

def index(request):
    # return HttpResponse("this is homepage")
    context = {
        'variable':"this is sent"
    }
    return render(request,'index.html',context)


def about(request):
    return render(request,'about.html')


def services(request):
    return render(request,'services.html')


def contact(request):
    if request.method=='POST':
        firstName=request.POST.get('firstName')
        lastName=request.POST.get('lastName')
        City=request.POST.get('city')
        Zip=request.POST.get('zip')
        contact= Contact(firstName=firstName,lastName=lastName,City=City,Zip=Zip)
        contact.save()
    return render(request,'contact.html')
