from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext as _

from .forms import EventForm


def event_list(request):
    return render(request, 'event/event_list.html', {})


def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            messages.success(request, _('Event successfully created.'))
            return redirect('event:list')
    else:
        form = EventForm()

    return render(request, 'event/event_create.html', {'form': form})
