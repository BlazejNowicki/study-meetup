from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext as _
from django.shortcuts import get_object_or_404

from catalog.models import Follower

from .forms import EventForm
from .models import Event


def event_list(request):
    if not request.user.is_authenticated:
        return redirect('/user/')

    followers = Follower.objects.filter(student=request.user)
    ids = [follower.course.id for follower in followers]
    events = Event.objects.filter(pk__in=ids)
    return render(request, 'event/event_list.html', {'events': events})


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'event/event_detail.html', {'event': event})


def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            messages.success(request, _('Event successfully created.'))
            return redirect('event:list')
    else:
        form = EventForm()

    return render(request, 'event/event_create.html', {'form': form})
