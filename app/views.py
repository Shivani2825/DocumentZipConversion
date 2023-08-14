from django.shortcuts import render
from .models import Person, Files
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.http import HttpResponse
from zipfile import ZipFile
import os

def signuppage(request):
    return render(request,'signuppage.html')


def saveuser(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        if Person.objects.filter(email=email).exists():
            messages.error(request,'Email Already Exists')
            return render(request,'signuppage.html')
        contact=request.POST['contact']
        password=request.POST['password']
        pwd=make_password(password)
        user=Person.objects.create(name=name,email=email,contact=contact,password=pwd)
        user.save
        return render(request,'login.html')
    return render(request,'signuppage.html')


def loginpage(request):
    return render(request,'login.html')

def loginuser(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']

        if Person.objects.filter(email=email).exists():
            obj=Person.objects.get(email=email)
            pwd=obj.password

            if check_password(password,pwd):
                return render(request,'uploadfile.html',{'obj':obj})
            else:
                messages.error(request,'Incorrect Password')
                return render(request,'login.html')
        else:
            messages.error(request,"Email doesn't exists")
            return render(request,'login.html')
        
    return render(request,'login.html')


def upload(request):
    if request.method == "POST":
        userid = request.POST.get('id')
        profile = request.FILES.get('profile')
        aadhar = request.FILES.get('aadhar')
        pancard = request.FILES.get('pancard')
        marksheet = request.FILES.get('marksheet')

        if Files.objects.filter(user_id=userid).exists():  # Use user_id instead of id
            fileobj = Files.objects.get(user_id=userid)  # Use user_id instead of id
            person = Person.objects.get(id=userid)  
            return render(request, 'download.html', {'data': fileobj, 'person': person, 'message': "Your documents already uploaded, You can download them."})
        else:
            person = Person.objects.get(id=userid)
            data = Files.objects.create(user=person, profile=profile, aadharcard=aadhar, pancard=pancard, marksheet=marksheet)  # Use correct field names
            return render(request, 'download.html', {'data': data, 'person': person, 'message': "Your documents successfully uploaded, You can download them."})

    return render(request, 'upload.html')  # Render the upload form template for GET requests

def download(request, id):
    user = Person.objects.get(id=id)
    files = Files.objects.filter(user=user)
    response = HttpResponse(content_type='application/zip')
    zip_filename = f'{user.name}_files.zip'
    response['Content-Disposition'] = f'attachment; filename="{zip_filename}"'

    with ZipFile(response, 'w') as zip_file:
        for file in files:
            zip_file.write(file.profile.path, os.path.basename(file.profile.path))
            zip_file.write(file.aadharcard.path, os.path.basename(file.aadharcard.path))
            zip_file.write(file.pancard.path, os.path.basename(file.pancard.path))
            zip_file.write(file.marksheet.path, os.path.basename(file.marksheet.path))

    return response