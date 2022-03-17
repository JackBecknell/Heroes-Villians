from django.db import models
from super_types.models import SuperTypes

class Super(models.model):
    name = models.CharField(maxlength=255)
    alter_ego = models.CharField(maxlength=255)
    primary_ability = models.CharField(maxlength=255)
    secondary_ability = models.CharField(maxlength=255)
    catchphrase = models.CharField(maxlength=255)
    super_type = models.ForeignKey(SuperTypes, on_delete=models.PROTECT)
