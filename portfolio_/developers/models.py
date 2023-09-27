from django.db import models

class Programmer(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    language = models.CharField(max_length=100)
    framework = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} {self.surname}"


# Create your models here.
