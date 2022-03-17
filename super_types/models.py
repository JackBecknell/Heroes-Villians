from django.db import models

class SuperTypes(models.model):
    name = models.CharField(max_length=255)
