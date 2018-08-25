from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        # The user wants to sign up!
        if request.POST['password1'] == request.POST['password2']:
            username = request.POST['username']
            password = request.POST['password1']
            signup_error = {'error':'Username exist!'}

            try:
                user = User.objects.get(username=username)
                return render(request, 'accounts/signup.html', signup_error) 
            except User.DoesNotExist:
                user = User.objects.create_user(username=username, password=password)
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error':'Passwords must match!'}) 

    else:
        # User wants to enter info
        return render(request, 'accounts/signup.html')
    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            login_error = {'error': 'Username or password is incorrect.'}
            return render(request, 'accounts/login.html', login_error)

    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

    # TODO Need to route to homepage
    # and don't foreget to logout


    return render(request, 'accounts/logout.html')
