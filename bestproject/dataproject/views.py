from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect
# from .read_model import predict_image
# from pathlib import Path
from .models import Image


# Create your views here.
def main(request):
    return render(request, 'dataproject/index.html', {})


@login_required
def user_logout(request):
    logout(request)
    return redirect('main')


def user_signup(request):
    if request.method == 'GET':
        return render(request, 'dataproject/registration.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                return redirect('user_login')
            except IntegrityError as err:
                return render(request, 'dataproject/registration.html',
                              {'form': UserCreationForm(), 'error': 'Username already exist!'})
        else:
            return render(request, 'dataproject/registration.html',
                          {'form': UserCreationForm(), 'error': 'Password did not match'})


def user_login(request):
    print('begin')
    if request.method == 'GET':
        print('get')
        return render(request, 'dataproject/login.html', {'form': AuthenticationForm()})
    else:
        print('not get', request.POST['username'], request.POST['password'])
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        print(user)
        if user is None:
            return render(request, 'dataproject/login.html',
                          {'form': AuthenticationForm(), 'error': 'Username or password didn\'t match'})
        login(request, user)
        return redirect('main')


@login_required
def upload_photo(request):
    if request.method == 'POST' and request.POST.get('myfile', None):
        image = request.POST.get('myfile', None)
        new_file = Image(user_id=request.user.id, image=image)
        new_file.save()
        all_photos = Image.objects.filter(user_id=request.user.id).all()
        for i in all_photos:
            print(i.image)
        return render(request, 'dataproject/storage.html', {'photos': all_photos})
    if request.method == 'GET':
        return render(request, 'dataproject/storage.html')


@login_required
def storage(request):
    if request.method == 'POST':
        all_photos = Image.objects.filter(user_id=request.user).all()
        print(all_photos)
        return render(request, 'dataproject/storage.html')
