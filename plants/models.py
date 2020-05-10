from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

class Plant(models.Model):
    objects = None
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200, null=True)
    is_active = models.BooleanField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "Plant"

    def __str__(self):
        return self.name

class GroupWisePlant(models.Model):
    objects = None
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "GroupWisePlant"
