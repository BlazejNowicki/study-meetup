from django.shortcuts import render


def event_list(request):
    return render(request, 'event/event_list.html', {})
