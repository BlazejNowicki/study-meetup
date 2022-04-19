from datetime import datetime
from django.forms import DateTimeField
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext as _
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.utils.timezone import now

from catalog.models import Follower

from .forms import EventForm
from .models import Event, Proposition, PropositionVote


def event_list(request):
    if not request.user.is_authenticated:
        return redirect('/user/')

    followers = Follower.objects.filter(student=request.user)
    ids = [follower.course.id for follower in followers]
    events = Event.objects.filter(pk__in=ids)
    return render(request, 'event/event_list.html', {'events': events})


def event_detail(request, pk):
    if not request.user.is_authenticated:
        redirect("/user/")

    event = get_object_or_404(Event, pk=pk)

    if request.method == "POST":
        if 'vote' in dict(request.POST):
            proposition_id = int(request.POST['vote'])
            proposition_vote = PropositionVote.objects.filter(author=request.user, proposition_id=proposition_id)
            if not proposition_vote.exists():
                PropositionVote(proposition=list(Proposition.objects.filter(id=proposition_id))[0],
                                author=request.user,
                                datetime=now).save()
        
        if 'date' in dict(request.POST):
            # print(request.POST['date'])
            dt = datetime.strptime(request.POST['date'], '%Y-%m-%dT%H:%M')
            Proposition(author=request.user,
                        event=event,
                        datetime=dt).save()

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
    return render(request, 'event/event_detail.html', {'event': event, 'propositions': propositions})


def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            messages.success(request, _('Event successfully created.'))
            return redirect('event:list')
    else:
        form = EventForm()
    return render(request, 'event/event_create.html', {'form': form})
