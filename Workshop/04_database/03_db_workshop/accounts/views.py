from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login     # login->auth_login 이름 변경
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm


# Create your views here.



def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 회원가입 후 로그인
            auth_login(request, user)
            return redirect('todos:index')
    else:
        form = CustomUserCreationForm
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            #로그인
            auth_login(request, form.get_user())
            return redirect('todos:index')
    else:
        form = AuthenticationForm
    context = {
        'form':form,
    }
    return render(request, 'accounts/login.html', context)