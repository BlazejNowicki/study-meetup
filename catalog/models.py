from django.db import models


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
        return f"{self.name} {self.university}"


class Discipline(models.Model):
    name = models.CharField(max_length=128)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "disciplines"

    def __str__(self):
        return f"{self.name} {self.faculty}"


class Course(models.Model):
    name = models.CharField(max_length=128)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "courses"

    def __str__(self):
        return f"{self.name}"