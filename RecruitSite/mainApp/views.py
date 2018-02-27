from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):

    stories = Story.objects.all()

    context = {
        'stories': stories
    }

    return render(request, 'mainApp/header.html', context)


def personal(request, num):

    story = Story.objects.get(person=Person.objects.get(id=num))

    job_history = Story.objects.filter(subdivision=story.subdivision, specialization=story.specialization)

    context = {
        'story': story,
        'jobs': job_history
    }

    return render(request, 'mainApp/person.html/', context)


def filtering(request):
    
    
    # Here's an error
    story = Story.objects.filter(person=Person.objects.filter(male=request.POST.get('male')),
                                 subdivision=Subdivision.objects.filter(branch=Branch.objects.filter(company=Company.objects.filter(id=request.POST.get('company')))),
                                 specialization=Specialization.objects.filter(id=request.POST.get('specialization')))


    context = {
        'story': story
    }

    return render(request, 'mainApp/header.html', context)