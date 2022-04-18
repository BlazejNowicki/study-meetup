from django.contrib import admin

from . import models

admin.site.register([models.University, models.Faculty, models.Discipline, models.Course, models.Follower])
