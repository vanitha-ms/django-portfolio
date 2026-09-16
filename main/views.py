from django.shortcuts import render, redirect
from .models import Profile, Skill, Project, Contact


def home(request):
    profile = Profile.objects.first()
    return render(request, "main/home.html", {
        "profile": profile
    })


def about(request):
    profile = Profile.objects.first()
    return render(request, "main/about.html", {
        "profile": profile
    })


def skills(request):
    skills = Skill.objects.all()
    return render(request, "main/skills.html", {
        "skills": skills
    })


def projects(request):
    projects = Project.objects.all()
    return render(request, "main/projects.html", {
        "projects": projects
    })


def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            message=request.POST.get("message")
        )
        return redirect("contact")

    return render(request, "main/contacts.html")