from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=200, default='< no title >')
    decription = models.TextField(blank=True)
    creation_date = models.DateField(auto_now_add=True)
    # importance = (
    #     ('High', 'It\'s important'),
    #     ('Common', 'Common task'),
    #     ('Low', 'Just trifle')
    # )
    # importance = models.CharField(max_length=100, choices=importance)
    important = models.BooleanField(default=False)
    deadline = models.DateField(null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default='1')

    def __str__(self):
        return self.title