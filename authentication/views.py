from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import check_password

def register(request) :
    if request.method == 'POST' :
        first_name = request.POST.get("first_name")
        last_name  = request.POST.get("last_name")
        email = request.POST.get("email")  
        pass_1 = request.POST.get("pass1")  
        pass_2 = request.POST.get("pass2")
        username = request.POST.get('username')
        user =  User.objects.filter(username = username)
        if user.exists() :
            messages.info(request,"User name is already Taken")
            return redirect('/register/')
        
        if pass_1 == pass_2 :
            user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email ,
            username = username,

        )
            user.set_password(pass_1)
            user.save()

            messages.info(request,"Account Created SucsessFully")
            return redirect('/register/')

        else :
            messages.info(request,"Password Isnt match")

            return redirect('/register/')
 
    return render(request,'registerpage.html')

def login(request) :
    if request.method == 'POST' :
        username = request.POST.get('username')
        passwaord1 = request.POST.get('password')

        user = User.objects.filter(username=username)

        user = user.first()

        if user :
            userspassword = user.password
            is_valid = check_password(passwaord1,userspassword)

            if is_valid :
                return redirect("home_app:home",username=user.username)
        
        else :

            messages.info(request,"No user have username like This !!!")
            return redirect('/login/')

    
        

    return render(request,'loginpage.html')