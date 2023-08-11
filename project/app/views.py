from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import Registration, User_files
import zipfile
from django.http import HttpResponse
import os
from django.shortcuts import get_object_or_404



def registrationpage(request):
    return render(request, 'signup.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        contact=request.POST['contact']
        email = request.POST['email']
        address=request.POST['address']
        password= request.POST['password']
        if Registration.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered. Please use a different email.')
            return render(request,'signup.html')
        password_hashed = make_password(password)
        user = Registration.objects.create(
            name=name,contact=contact, email=email, address=address,password=password_hashed)
        user.save()
        return render(request,'login.html')

    return render(request, 'signup.html')

def loginpage(request):
    return render(request, 'login.html')

def login(request):
    if request.method == "POST":
        if 'email' in request.POST:
            email = request.POST['email']
            User_password = request.POST['password']

            if Registration.objects.filter(email=email).exists():
                obj = Registration.objects.get(email=email)
                password = obj.password

                if check_password(User_password, password):
                    return render(request, 'uploadfile.html', {'obj':obj})
                else:
                    messages.error(request, 'Password Incorrect')
                    return render(request,'login.html')
            else:
                messages.error(request, 'Email is not registered')
                return render(request,'login.html')
        else:
            messages.error(
                request, 'Email field is missing in the form submission')
            return render(request,'login.html')
    return render(request, 'login.html')

# @login_required
def upload_files(request):
    return render(request, 'uploadfile.html')

# @login_required
def upload_files_data(request):
    if request.method == 'POST':
        user_id = request.POST['id']
        profile_photo = request.FILES.get('profile_photo')
        aadhar_card = request.FILES.get('aadhar_card')
        pan_card = request.FILES.get('pan_card')
        voter_id = request.FILES.get('voter_id')
        marksheet = request.FILES.get('marksheet')

        if User_files.objects.filter(userid=user_id).exists():
            person=Registration.objects.get(id=user_id)
            data = User_files.objects.get(userid=user_id)
            return render(request, 'downloadpg.html', {'user': data,'person':person,'message':"Your documents already uploaded, You can download them"})

        else:
            user = User_files.objects.create(userid=user_id, profile_photo=profile_photo, aadhar_card=aadhar_card,
                                             pan_card=pan_card, voter_id=voter_id, marksheet=marksheet)
            print(user)
            if User_files.objects.filter(userid=user_id).exists():
                person=Registration.objects.get(id=user_id)
                data = User_files.objects.get(userid=user_id)
                return render(request, 'downloadpg.html', {'user': data,'person':person, 'message':"Your documents successfully uploaded, You can download them"})

# @login_required
def download_files_as_zip(request, user_id):
    if request.method == 'GET':
        user = User_files.objects.get(userid=user_id)
        user_registration = get_object_or_404(Registration, id=user.userid)
        files_to_download = [
            user.profile_photo,
            user.aadhar_card,
            user.pan_card,  
            user.voter_id,
            user.marksheet
        ]
        memory_file = zipfile.ZipFile('files.zip', 'w')
        for file_to_download in files_to_download:
            if file_to_download:
                memory_file.write(file_to_download.path, file_to_download.name)
        memory_file.close()
        response = HttpResponse(content_type='application/zip')
        response['Content-Disposition'] = f'attachment; filename="{user_registration.name}_files.zip"'

        with open('files.zip', 'rb') as f:
            response.write(f.read())
        memory_file.close()
        os.remove('files.zip')

        return response
