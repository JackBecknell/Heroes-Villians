from django.db import models

class SuperTypes(models.Model):
    name = models.CharField(max_length=255)
