from django.db import models


# Create your models here.
class Door(models.Model):
    open = models.BooleanField()

    class Meta:
        db_table = "Door"


class Trash(models.Model):
    date = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=15)
    type_probability = models.FloatField()
    foreign_subst = models.CharField(max_length=50)
    foreign_subst_probability = models.CharField(max_length=500)
    image = models.CharField(max_length=300)
    feedback_type = models.CharField(max_length=15, blank=True, null=True)
    feedback_foreign_subst = models.BooleanField(blank=True, null=True)
