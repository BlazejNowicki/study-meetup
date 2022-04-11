from django.contrib import admin

from .models import Event, Proposition, PropositionVote

admin.site.register([Event, Proposition, PropositionVote])
