from django.shortcuts import render , redirect
from django.http import HttpResponse

# Create your views here.

def home(request):
    context = {'name': 'User', 'items': [1, 2, 3]}
    return render(request , 'index.html' , context)

def login_page(request):
    context = {'name':"loginpage"}
    return render(request , 'loginpage.html' ,context)


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # name = request.POST.get("username")
        
        print("Name:", username)
        print("pass:", password)

        return redirect('/'  , local="mayur")