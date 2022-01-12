from django.shortcuts import render
from .forms import ProjectForm
from .models import Project


def index(request):
    return render(request, 'modelForms/index.html')


def listProjects(request):
    projectsList = Project.objects.all()
    return render(request, 'modelForms/listProjects.html', {'projects': projectsList})


def addProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    return render(request, 'modelForms/addProject.html', {'form': form})
