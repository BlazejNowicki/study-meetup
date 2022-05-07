from datetime import datetime
import os, sys
import django

sys.path.append('/code')
os.environ['DJANGO_SETTINGS_MODULE'] = 'study_meetup.settings'
django.setup()


from catalog.models import Course, Discipline, Faculty, Follower, University
from event.models import Event, Proposition, PropositionVote
from django.contrib.auth.models import User
agh = University.objects.create(name="AGH")
uj = University.objects.create(name="UJ")

wmif = Faculty.objects.create(name="WMiF", university=uj)
wiet = Faculty.objects.create(name="WIET", university=agh)
weiiib = Faculty.objects.create(name="WEIiIB", university=agh)

sc = Discipline.objects.create(name="Informatyka", faculty=wiet)
si = Discipline.objects.create(name="Informatyka i systemy inteligentne", faculty=weiiib)
ss = Discipline.objects.create(name="Cyberbezpieczeństwo", faculty=wiet)
tcs = Discipline.objects.create(name="Matematyka komputerowa", faculty=wmif)

alg = Course.objects.create(name="Algebra", discipline=sc)
am = Course.objects.create(name="Analiza matematyczna I", discipline=sc)
am2 = Course.objects.create(name="Analiza matematyczna II", discipline=sc)
ps = Course.objects.create(name="Programowanie skryptowe", discipline=ss)
alg2 = Course.objects.create(name="Algebra", discipline=si)
stat = Course.objects.create(name="Statystyka", discipline=tcs)

jan = User.objects.create_user('jankowalski', 'jan.kowalski@gmail.com', 'jankowalski')
anna = User.objects.create_user('annanowak', 'anna.nowak@gmail.com', 'annanowak')
kamil = User.objects.create_user('kamilkowalczyk', 'kamil.kowalczyk@gmail.com', 'kamilkowalczyk')

Follower.objects.create(student=jan, course=alg)
Follower.objects.create(student=jan, course=am)
Follower.objects.create(student=jan, course=am2)

Follower.objects.create(student=anna, course=alg)
Follower.objects.create(student=anna, course=am)
Follower.objects.create(student=anna, course=am2)

Follower.objects.create(student=kamil, course=alg)
Follower.objects.create(student=kamil, course=stat)
Follower.objects.create(student=kamil, course=am2)

e1 = Event.objects.create(name="Kolokwium macierze", author=jan, course=alg, status=1, description="Powtórzenie teorii i zadania")
e2 = Event.objects.create(name="Kolokwium całki", author=anna, course=am, status=2, description="...")

p1 = Proposition.objects.create(author=jan, event=e1, datetime=datetime(2022, 5, 11, 18, 0))
p2 = Proposition.objects.create(author=jan, event=e1, datetime=datetime(2022, 5, 12, 20, 30))
p3 = Proposition.objects.create(author=anna, event=e1, datetime=datetime(2022, 5, 11, 22, 0))

pv1 = PropositionVote.objects.create(proposition=p1, author=jan, datetime=datetime(2022, 5, 9, 20, 0))
pv2 = PropositionVote.objects.create(proposition=p2, author=jan, datetime=datetime(2022, 5, 9, 21, 0))
pv3 = PropositionVote.objects.create(proposition=p1, author=anna, datetime=datetime(2022, 5, 9, 22, 0))
pv3 = PropositionVote.objects.create(proposition=p1, author=kamil, datetime=datetime(2022, 5, 9, 23, 0))

p4 = Proposition.objects.create(author=jan, event=e2, datetime=datetime(2022, 5, 10, 10, 0))
p5 = Proposition.objects.create(author=anna, event=e2, datetime=datetime(2022, 5, 11, 11, 15))

pv1 = PropositionVote.objects.create(proposition=p4, author=jan, datetime=datetime(2022, 5, 9, 20, 0))
pv2 = PropositionVote.objects.create(proposition=p5, author=jan, datetime=datetime(2022, 5, 9, 21, 0))
pv3 = PropositionVote.objects.create(proposition=p4, author=anna, datetime=datetime(2022, 5, 9, 22, 0))