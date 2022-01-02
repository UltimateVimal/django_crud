from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from core.forms import AddStudentForm
from .models import Student

def Home(request):
    return render(request,'core/home.html')

def AddStudent(request):
    if request.method=='POST':
        frm=AddStudentForm(request.POST)
        if frm.is_valid():
            frm.save()
            return redirect('/')
    else:
        fm=AddStudentForm()
        return render(request,'core/add_student.html',{'form':fm})

def DisplayAll(request):
    stData=Student.objects.all()
    return render(request,'core/display_all.html',{'alldata':stData})

def DeleteStudent(request):
    if request.method=='POST':
        stid=request.POST['hdStId']
        StudData=Student.objects.get(id=stid)
        StudData.delete()
        return redirect('/')
    else:
        stData=Student.objects.all()
        return render(request,'core/delete_student.html',{'alldata':stData})

