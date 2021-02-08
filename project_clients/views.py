from django.shortcuts import render
from django.contrib import messages, auth
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404



def client_profile(request):
    return render(request, 'client/profile/client_profile.html')


def edit_client_profile(request):
    return render(request, 'client/profile/edit_client_profile.html')


def edit_client_password(request):
    return render(request, 'client/profile/change_password.html')



def client_logout(request):
    logout(request)
    return redirect('client-login')
