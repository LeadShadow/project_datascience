import os
from pathlib import Path

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db import IntegrityError
from django.shortcuts import render, redirect
# from .read_model import predict_image
# from pathlib import Path
from .models import Image
from .load_download_img import download_user_image, load_for_user
from .read_model import predict_image

BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_DIR = Path('temp/')
image_list = []

# Create your views here.
def main(request):
    # if request.method == 'POST' and request.FILES['myfile']:
    #     file = request.FILES['myfile']

    if request.method == 'POST' and request.FILES.get('myfile', None):
        file = request.FILES.get('myfile', None)
        if file is not None and Path(file.name).suffix[1:].upper() in ('JPEG', 'JPG', 'PNG', 'SVG', 'ICO', 'BMP'):
            if os.path.exists(UPLOAD_DIR / file.name):
                os.remove(UPLOAD_DIR / file.name)
            fs = FileSystemStorage(UPLOAD_DIR)
            filename = fs.save(file.name, file)
            filepath = UPLOAD_DIR / filename
            get_id_img = download_user_image(filepath, filename)
            class_img = predict_image(filepath)
            # class_img = 'professor'
            new_string = Image(user_id=request.user.id, image_id=get_id_img, image_class=class_img)
            new_string.save()
            # new_file = Image(user_id=request.user.id, image=image)
            # new_file.save()
            # all_photos = Image.objects.filter(user_id=request.user.id).all()
            # for i in all_photos:
            #     print(i.image)
            image_list = load_for_user(request.user.id)
            return render(request, 'dataproject/storage.html', {'photos': image_list[::-1]})
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
    global image_list
    print('begin')
    if request.method == 'GET':
        print('get')
        return render(request, 'dataproject/login.html', {'form': AuthenticationForm()})
    else:
        print('not get', request.POST['username'], request.POST['password'])
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'dataproject/login.html',
                          {'form': AuthenticationForm(), 'error': 'Username or password didn\'t match'})
        login(request, user)
        return redirect('main')


# @login_required
# def upload_photo(request):
#
#     if request.method == 'POST' and request.POST.get('myfile', None):
#         image = request.POST.get('myfile', None)
#         new_file = Image(user_id=request.user.id, image=image)
#         new_file.save()
#         all_photos = Image.objects.filter(user_id=request.user.id).all()
#         for i in all_photos:
#             print(i.image)
#         return render(request, 'dataproject/storage.html', {'photos': all_photos})
#     if request.method == 'GET':
#         return render(request, 'dataproject/storage.html')


@login_required
def storage(request):
    print('######')
    image_list = load_for_user(request.user.id)
    return render(request, 'dataproject/storage.html', {'photos': image_list[::-1]})
