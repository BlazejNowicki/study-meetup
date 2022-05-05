from django.db import models
from django.contrib.auth.models import User


class University(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name_plural = "universities"

    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length=128)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "faculties"

    def __str__(self):
        return f"{self.name}"


class Discipline(models.Model):
    name = models.CharField(max_length=128)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "disciplines"

    def __str__(self):
        return f"{self.name}"


class Course(models.Model):
    name = models.CharField(max_length=128)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "courses"

    def __str__(self):
        return f"{self.name}"


class Follower(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student} {self.course}"
