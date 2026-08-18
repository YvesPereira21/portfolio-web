from django.shortcuts import render, get_object_or_404
from .models import AboutMe, Project, Formation, Certificate

def home(request):
    about_me = AboutMe.objects.first()
    return render(request, "portfolio/pages/aboutme.html", {"about_me": about_me})

def projects(request):
    projects_list = Project.objects.all()
    return render(request, "portfolio/pages/projects.html", {"projects": projects_list})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, "portfolio/pages/project_detail.html", {"project": project})

def education(request):
    formations = Formation.objects.all().order_by('-start_date')
    certificates = Certificate.objects.all().order_by('-issue_date')
    return render(request, "portfolio/pages/education.html", {
        "formations": formations,
        "certificates": certificates,
    })




