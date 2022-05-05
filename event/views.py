from datetime import datetime

from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext as _
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.utils.timezone import now

from catalog.models import Follower, Course

from .forms import EventForm
from .models import Event, Proposition, PropositionVote


def event_list(request):
    if not request.user.is_authenticated:
        return redirect('/user/')

    name = request.GET.get('name', '')
    status = int(request.GET.get('status', 0))

    followers = Follower.objects.filter(student=request.user)
    ids = [follower.course.id for follower in followers]

    if status != 0:
        events = Event.objects.filter(course__id__in=ids, name__icontains=name, status=status).order_by('-id')
    else:
        events = Event.objects.filter(course__id__in=ids, name__icontains=name).order_by('-id')

    return render(request, 'event/event_list.html', {'events': events})


def event_detail(request, pk):
    if not request.user.is_authenticated:
        redirect("/user/")

    event = get_object_or_404(Event, pk=pk)

    if request.method == "POST":
        if 'vote' in dict(request.POST) and event.is_waiting():
            proposition_id = int(request.POST['vote'])
            proposition_vote = PropositionVote.objects.filter(author=request.user, proposition_id=proposition_id)
            if not proposition_vote.exists():
                PropositionVote(proposition=list(Proposition.objects.filter(id=proposition_id))[0],
                                author=request.user,
                                datetime=now).save()
        
        if 'date' in dict(request.POST) and event.is_waiting():
            dt = datetime.strptime(request.POST['date'], '%Y-%m-%dT%H:%M')
            Proposition(author=request.user, event=event, datetime=dt).save()

        if 'close' in dict(request.POST) and event.is_waiting():
            if request.user != event.author:
                raise Http404()
            event.set_status_approved()
            event.save()
            messages.success(request, 'Event successfully closed.')

        if 'archive' in dict(request.POST) and event.is_approved():
            if request.user != event.author:
                raise Http404()
            event.set_status_archived()
            event.save()
            messages.success(request, 'Event successfully modified.')

    propositions = list(Proposition.objects.filter(event=event))
    votes = PropositionVote.objects.values('proposition').annotate(total=Count('proposition')).order_by('proposition')

    votes_as_dict = {}
    for vote in votes:
        votes_as_dict[vote['proposition']] = vote['total']
    
    for prop in propositions:
        if prop.id in votes_as_dict.keys():
            prop.votes = votes_as_dict[prop.id]
            prop.voted = PropositionVote.objects.filter(author=request.user, proposition_id=prop.id).exists()
        else:
            prop.votes = 0
            prop.voted = False

    propositions.sort(key=lambda x: x.votes, reverse=True)
    return render(request, 'event/event_detail.html', {'event': event, 'propositions': propositions})


def event_create(request):
    if request.method == 'POST':
        form = EventForm(request, request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            course = form.cleaned_data.get('course')
            description = form.cleaned_data.get('description')

            course = Course.objects.get(pk=int(course))
            event = Event(name=name, author=request.user, course=course, description=description)
            event.save()

            messages.success(request, _('Event successfully created.'))
            return redirect('event:list')
    else:
        form = EventForm(request)
    return render(request, 'event/event_create.html', {'form': form})
