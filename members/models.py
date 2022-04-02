from django.db import models


class Members(models.Model):
    objects = None
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
