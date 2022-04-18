from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    lead = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lead')
    user_work_on = models.ManyToManyField(User)


class Ticket(models.Model):
    STATUS_CHOICES = [
        (1, 'New'),
        (2, 'Open'),
        (3, 'Active'),
        (4, 'Closed')
    ]
    PRIORITY_CHOICES = [
        (1, 'High'),
        (2, 'Medium'),
        (3, 'Low')
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='New')

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_to = models.ManyToManyField(User)
