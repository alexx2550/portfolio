from django.contrib.auth.models import User
from django.db import models

class Programmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    language = models.CharField(max_length=200)
    framework = models.CharField(max_length=200)
    experience = models.IntegerField()

    def __str__(self):
        return self.user.get_full_name()


class Project(models.Model):
    foreign_key = models.ForeignKey(Programmer, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
# Create your models here.
