from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseForm


def getInstructors(request):
    instructors = Course.objects.all()
    return render(request, 'courseApp/index.html', {'instructors': instructors})


def createInstructor(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'courseApp/create.html', {'form': form})


def deleteInstructor(request, id):
    instructor = Course.objects.get(id=id)
    instructor.delete()
    return redirect('/')


def updateInstructor(request, id):
    instructor = Course.objects.get(id=id)
    form = CourseForm(instance=instructor)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=instructor)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'courseApp/update.html', {'form': form})


def logout(request):
    return render(request, 'courseApp/logout.html')
