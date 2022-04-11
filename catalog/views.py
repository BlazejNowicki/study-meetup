from django.shortcuts import render


def index(request):
    return render(request, "catalog/course_list.html", {})
