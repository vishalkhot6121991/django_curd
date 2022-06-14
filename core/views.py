
from django.shortcuts import redirect, render
from django.views import View
from .models import student
from .forms import addstudentform
# Create your views here.
class Home(View):
    def get(self, request):
        sut_data=student.objects.all()
        return render(request,'core/home.html',{'studata':sut_data})
    
class student_view(View):
    def get(self,request):
        fm=addstudentform()
        return render(request,'core/add_student.html',{'form':fm})
    
    def post(self,request):
        fm=addstudentform(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request,'core/add_student.html',{'form':fm})
class Delete_student(View):
    def post(self,request):
        data=request.POST
        id=data.get('id')
        studata=student.objects.get(id=id)
        studata.delete()
        return redirect('/')
class Editstudent(View):
    def get(self,request,id):
        stu=student.objects.get(id=id)
        fm=addstudentform(instance=stu)
        return render(request,'core/edit_student.html',{'form':fm})
    def post(self,request,id):
        stu=student.objects.get(id=id)
        fm=addstudentform(request.POST,instance=stu)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        
        
        