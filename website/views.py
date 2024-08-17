from django.shortcuts import render
from django.http import HttpResponse


def about_view(request):
    return render(request, 'website/about.html')

def resume_view(request):
    return render(request, 'website/resume.html')

def project_view(request):
    return render(request, 'website/projects.html')

def project_single_view(request):
    return render(request, 'website/project_main.html')