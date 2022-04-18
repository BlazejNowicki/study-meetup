from sys import stdout
from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Course, Discipline, Follower


def catalog_root(request):
    if not request.user.is_authenticated:
        return redirect("/user/")

    if request.method == "POST":
        post_data = dict(request.POST.lists())
        if 'remove' in post_data.keys():
            for id in post_data['remove']:
                Follower.objects.filter(student=request.user, course=id).delete()

        if 'add' in post_data.keys():
            for id in post_data['add']:
                course = Course.objects.get(id=id)
                Follower(student=request.user, course=course).save()
    

    followers = Follower.objects.filter(student=request.user)
    all_courses = Course.objects.all()
    for follower in followers:
        all_courses = all_courses.all().exclude(id=follower.course.id)

    return render(request, 'catalog/root.html', { 'saved': followers, 'all': all_courses})


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
