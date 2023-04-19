from django.shortcuts import render

            
from app1.forms import *
from app1.models import *
from django.http import HttpResponse

def Insert_student(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        FD=StudentForm(request.POST)
        if FD.is_valid():
            sid=FD.cleaned_data['sid']
            name=FD.cleaned_data['name']
            mobile=FD.cleaned_data['mobile']
            email=FD.cleaned_data['email']
            SO=Student.objects.get_or_create(sid=sid,name=name,mobile=mobile,email=email)[0]
            SO.save()

            SQS=Student.objects.all()
            d1={'SQS':SQS}
            return render(request,'display_Student.html',d1)

    return render(request,'Insert_student.html',d)

def Insert_Course(request):
    COD=CourseForm()
    d={'COD':COD}
    if request.method=='POST':
        CD=CourseForm(request.POST)
        if CD.is_valid():
            cid=CD.cleaned_data['cid']
            sid=CD.cleaned_data['sid']
            cname=CD.cleaned_data['cname']
            Ctrianer=CD.cleaned_data['Ctrianer']
            SO=Student.objects.get_or_create(sid=sid)[0]
            SO.save()
            CO=Course.objects.get_or_create(sid=SO,cid=cid,cname=cname,Ctrianer=Ctrianer)[0]
            CO.save()

            SQS=Course.objects.all()
            d1={'SQS':SQS}
            return render(request,'Display_Course.html',d1)
    return render(request,'Insert_Course.html',d)