from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from users.forms import UserRegisterForm


# Create your views here.


def register_views(request):
    
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog:post-list')
        else:
            print(form.errors)
        
    else:
        form = UserRegisterForm()
    return render(request,
                  'users/user-register.html',
                  {'userform': form})


def login_views(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(request,
                                username=username,
                                password=password)
            
            if user is not None:
                login(request, user)
                return redirect('blog:post-list')
    else:
        form = AuthenticationForm()

    return render(request, 'users/user-login.html', {'auth_form': form})



def logout_views(request):
    
    if request.method == "POST":
        logout(request)
        return redirect('users:login')
    
    return render(request, 'users/user-logout.html')