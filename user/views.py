from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.http.response import Http404, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required


@login_required(login_url='/user/signin')
def user_home(request):
    return redirect('/catalog/')


def user_signin(request):
    if request.user.is_authenticated:
        return HttpResponseBadRequest()

    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)
            login(request, user)

            messages.success(request, _('Successfully login.'))
            return redirect('user:home')

    return render(request, 'user/user_signin.html', {'form': form})


def user_signup(request):
    if request.user.is_authenticated:
        return HttpResponseBadRequest()

    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(request, username=username, password=password)
            login(request, user)

            messages.success(request, _('Successfully signup.'))
            return redirect('user:home')

    return render(request, 'user/user_signup.html', {'form': form})


def user_logout(request):
    if not request.user.is_authenticated:
        raise Http404
    logout(request)
    messages.success(request, _('Logout successfully'))
    return redirect('catalog:root')
