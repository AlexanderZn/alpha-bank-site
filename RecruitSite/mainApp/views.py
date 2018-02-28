from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):

    stories = Story.objects.all()

    context = {
        'stories': stories,
        'form_data': stories
    }

    return render(request, 'mainApp/header.html', context)


def personal(request, num):

    stories = Story.objects.get(person=Person.objects.get(id=num))

    job_history = Story.objects.filter(subdivision=story.subdivision, specialization=story.specialization)

    context = {
        'stories': stories,
        'jobs': job_history
    }

    return render(request, 'mainApp/person.html/', context)


def filtering(request):
    
    
    # Here's an error 
    #stories = Story.objects.filter(person=Person.objects.filter(male=request.GET.get('male')),
    #                            subdivision=Subdivision.objects.filter(branch=Branch.objects.filter(company=Company.objects.get(id=request.GET.get('company')))),
    #                            specialization=Specialization.objects.get(id=request.GET.get('specialization')))

    stories = Story.objects.filter(person__male=request.GET.get('male'),
                                   subdivision__branch__company__id=request.GET.get('company', None),
                                   specialization__sphere__id=request.GET.get('sphere', None),
                                   specialization__id=request.GET.get('specialization', None))

    form_data = Story.objects.all()



    context = {
        'stories': stories,
        'form_data': form_data
    }

    return render(request, 'mainApp/header.html', context)
