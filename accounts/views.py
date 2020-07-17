from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, authenticate, get_user_model
from .forms import LoginForm, UserCreateForm, UserUpdateForm
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

User = get_user_model()

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'accounts/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'accounts/login.html'

class CreateAccount(CreateView):
    template_name = 'accounts/create.html'
    form_class = UserCreateForm
    model = User
    success_url = reverse_lazy('accounts:login')

class UpdateAccount(UpdateView):
    # template_name_suffix = '_update_form'
    template_name = 'accounts/update.html'
    form_class = UserUpdateForm
    model = User
    success_url = reverse_lazy('accounts:login')
