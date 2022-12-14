from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login
from .models import Account

# Create your views here.
def index(request):
  accounts = Account.objects.all()
  context = {
    'accounts': accounts,
  }
  return render(request, 'accounts/index.html', context)


def signup(request):
  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      # 회원가입 후 로그인
      auth_login(request, user)
      return redirect('accounts:index')
  else:
      form = CustomUserCreationForm()
  context = {
    'form': form,
  }
  return render(request, 'accounts/signup.html', context)