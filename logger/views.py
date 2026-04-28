from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from  django.contrib.auth.hashers import make_password ,check_password
from django.contrib import messages
from .models import user
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout 
from django.contrib.auth.decorators import login_required
# Create your views here.




# @login_required(login_url='/loginpage/')
def home(request):  
    data = user.objects.all(); 
    print(data)

    return render(request , 'index.html' , context={'data':data})

# def login_page(request):
#     context = {'name':"loginpage"}
#     return render(request , 'loginpage.html' ,context)

# @login_required(login_url='/loginpage/')
def newuser(request):
    if request.method == 'POST':
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        uname = request.POST.get('username')
        age = request.POST.get('age')
        password = request.POST.get('password')
        # password = make_password(request.POST.get('password'))
        obj = user(first_name=fname,last_name=lname,username=uname , age=age , password=password)
        if(user.objects.filter(username=uname).exists() ):
            print("username already exist")
            messages.error(request, "This username is already taken. Please choose another one.")
            return render(request, 'register.html')
        else:
            # user = User.objects.create_user(
            #     first_name=fname,
            #     last_name=lname,
            #     username=uname ,
            #     age=age, 
            #     password=password
            # )
            obj.save()
            return redirect("/")

# @login_required(login_url='/loginpage/')
def register(request):
    return render(request, 'register.html')

def logout_page(request):
    # logout(request )
    return redirect ('/loginpage/')


def login_page(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

    
        sessionUser = user.objects.filter(username=username).first()
        if(sessionUser):
            print(sessionUser.username)
            print(sessionUser.password)
            if(sessionUser.password == password):

                
                print("valid user")
                return redirect('/')
            else:
                messages.error(request, "incorrect password")
        else:
            print(username + " not exist")
            messages.error(request, "invalid username")
        # login(request , auth_user)/
            return redirect('/loginpage/')

        # if not user.objects.filter(username=username).exists():
        #     print(username)
        #     
        #     return redirect('/loginpage/')
        
        # auth_user = authenticate(username=username , password=password)
        # print("user is " + username)
        # if auth_user :
        #     login(request , auth_user)
        #     return redirect('/')
            
        # else:
        #     messages.error(request, "invalid password")
        #     return redirect('/loginpage/')
        #     print("rediectiong")
        
    return render(request , 'loginpage.html' )


def delete_person(request,person_username):
    Person = user.objects.filter(username=person_username).first()
    print(Person)
    Person.delete()
    return redirect('/')