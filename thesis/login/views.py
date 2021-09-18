from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model
from django.contrib import messages
from . import models
from datetime import datetime
from PyPDF2 import PdfFileReader, PdfFileWriter
from .models import thesis
import mimetypes

def home(request):
    return render(request, 'loginpage.html')

def fp(request):
    return render(request, 'fp.html')

def bank(request):
    return render(request, 'bank.html')

def upload(request):
    return render(request, 'thesis.html')

def admin(request):
    return render(request, 'admin.html')

def examiner(request):
    return render(request, 'examinor.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        examinor = request.POST.get('choice', None)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if examinor == '1' and user.is_staff:
                thesises = thesis.objects.all()
                return render(request, 'admin.html',{'thesises':thesises})

            elif examinor == '2' and not user.is_staff:
                thesises = thesis.objects.all()
                return render(request, 'examinor.html',{'thesises':thesises})

            elif examinor == '1' and not user.is_staff:
                messages.info(request, 'You are not an admin')
                return redirect('home')
            else:
                messages.info(request, 'Please select Admin or Examinor!')
                return redirect('home')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('home')

def logout(request):
    auth.logout(request)
    return render('home', request)

def upload2(request):
    if request.method == 'POST':
        TitleId = request.POST['TitleId']
        Student_Name = request.POST['Student_Name']
        time = datetime.now()
        Speciality = request.POST['Speciality']
        ExaminorId = request.POST['ExaminerId']
        filepass = time.date()
        Thesis_Type = request.POST['Thesis_Type']
        file = request.POST['file']
        name = Student_Name + '_' + Speciality
        apply_password(filepass, file, name)
        models.thesis(TitleId = TitleId, Student_Name = Student_Name, time = time.time(), date = time.date(), Speciality = Speciality, ExaminorId = ExaminorId, filepass = filepass, Thesis_Type = Thesis_Type, file = file)
        return redirect('admin')

def apply_password(pas, file, name):
    name = "C:/Users/anmol/projects/thesis/thesis/file/" + name
    reader = PdfFileReader(file)
    writer = PdfFileWriter()
    for pageNum in range(reader.numPages):
        writer.addPage(reader.getPage(pageNum))
    writer.encrypt(pas)
    resultPdf = open(name, 'wb')
    writer.write(resultPdf)
    resultPdf.close()
    

def download_file(request):
    # fill these variables with real values
    fl_path = '/file/path'
    filename = 'downloaded_file_name.extension'

    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response