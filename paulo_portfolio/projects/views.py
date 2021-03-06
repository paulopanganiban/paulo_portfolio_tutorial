from django.shortcuts import render
from .models import Project
# Create your views here.


def project_index(request):
    # sa view kumukuha ng data diba?
    # tas ipapasa natin sa html. so basic shit
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {'project': project}
    return render(request, 'projects/project_detail.html', context)
