from django.shortcuts import render ,redirect , get_object_or_404
from .models import student
from .form import studentForm
# Create your views here.
def home(request):
    return render(request,'student/home.html')
def studentf(request):
    return render(request,'student/student.html')
def exam(request):
    return render(request,'student/exam.html')
def about(request):
    return render(request,'student/exam.html')
def contactUs(request):
    return render(request,'student/exam.html')

def addhtml(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        yearOfstudy = request.POST.get('yearOfstudy')
        course = request.POST.get('course')

        student.objects.create(name = name , age = age , yearOfstudy = yearOfstudy , course = course)
        redirect ('/listviews')

    return render(request,'student/add.html')

# CRUD OPERATION 
#CREAT DATA
def addStudent(request):
    form = studentForm()
    if request.method == 'POST' :
        form = studentForm(request.POST)
        if form.is_valid :
            form.save()
            return redirect('listviews')
    return render(request , 'student/studentForm.html',{'form': form})

#Read  all data on a table
def listView(request):
    Student = student.objects.all()
    context = {'Student':Student}

    return render(request,'student/list.html',context)


#Update data 
def edit(request,id):
    Student = get_object_or_404(student,id = id)

    if request.method == "POST":
        Student.name = request.POST.get ('name')
        Student.age = request.POST.get ('age')
        Student.course = request.POST.get('course')
        Student.yearOfstudy = request.POST.get ('yearOfstudy')

        student.save()

        return redirect('/listviews')
    
    return render(request, 'student/update.html',{'Student': Student})

 # delete data

def delete(request,id):
    Student  = get_object_or_404(student,id = id)
    Student.delete()     
    
    return redirect('/listviews')



