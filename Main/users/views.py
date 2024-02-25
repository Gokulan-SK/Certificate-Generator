from django.shortcuts import render,redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth import login,authenticate


def home_page(request):
    return render(request,'index.html',{})


# Create your views here.
def login_page(request):
    if request.method=='POST':
        #retrieving username and password from login page
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        #validating the username and password by checking with the existing users. value will be 0 if the is no user found.
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user) #redirecting the user after successful login
            return render(request,'dashboard.html',{})
            
        else:
            #if controll is here then Authentication is failed 
            #so redirect the user to the login page again and send the message invalid username/password
            return render(request, 'authenticate\login.html', {'error_message': 'Invalid username or password'})


    return render(request,'authenticate\login.html',{})