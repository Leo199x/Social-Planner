from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    locationName = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.user

class Event(models.Model):
    eventName = models.CharField(max_length=300)
    date_added = models.DateField(auto_now_add=True)
    eventLocation = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.eventName

