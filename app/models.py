from django.db import models

class Document(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    file = models.FileField()