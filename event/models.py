from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

from catalog.models import Course

EVENT_STATUS = (
    (1, _('Waiting')),
    (2, _('Approved')),
    (3, _('Archived')),
)


class Event(models.Model):
    name = models.CharField(max_length=128, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    status = models.IntegerField(choices=EVENT_STATUS, default=1)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'events'

    def __str__(self):
        return self.name

    def status_to_str(self):
        return [s[1] for s in EVENT_STATUS if s[0] == self.status][0]

    def set_status_approved(self):
        self.status = 2


class Proposition(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    datetime = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'propositions'

    def __str__(self):
        return f'{self.event}'


class PropositionVote(models.Model):
    proposition = models.ForeignKey(Proposition, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('proposition', 'author')
        verbose_name_plural = 'proposition votes'

    def __str__(self):
        return f'{self.proposition} from {self.author}'
