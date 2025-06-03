from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    event_name = models.CharField(max_length=200)