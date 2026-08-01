from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForms,ProfileUpdateForms
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
        
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

def login(response):
    return render(response, 'users/login.html')

def logout(response):
    return render(response, 'users/logout.html')

@login_required
def profile(response):
    u_form = UserUpdateForms()
    p_form = ProfileUpdateForms()

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(response, 'users/profile.html', context)