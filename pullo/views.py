from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Shoes


# Create your views here.
def index(request):
    

    shoes=Shoes.objects.all()
    



    return (render(request,'index.html',{'shoes':shoes}))


def contact(request):
    return (render(request,'contact.html'))

def about(request):
    return (render(request,'about.html'))

def home(request):
    return redirect('/')

def brand(request):
    shoes=Shoes.objects.all()
    return render(request,'brand.html',{'shoes':shoes})

def redirectToBrand(request):
    return brand(request)


def detail(request, pk): 
   products=Shoes.objects.get(id=pk) 
   context={'products':products}
   return  render(request,"productDetails.html",context)

def command(request):
    return(render(request,'command.html'))