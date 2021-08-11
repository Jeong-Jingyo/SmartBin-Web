from django.db import models


# Create your models here.
class Door(models.Model):
    open = models.BooleanField()

    class Meta:
        db_table = "Door"
