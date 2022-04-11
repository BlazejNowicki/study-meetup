from django.shortcuts import render
from django.http import HttpResponse

from .models import Course, Discipline


def catalog_root(request):
    return render(request, 'catalog/root.html')


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'catalog/course_list.html', {'courses': courses})


def discipline_list(request):
    disciplines = Discipline.objects.all()
    return render(request, 'catalog/discipline_list.html', {'disciplines': disciplines})


def faculties_list(request):
    return HttpResponse("Faculties")


def universities_list(request):
    return HttpResponse("Universities")

