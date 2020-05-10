from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

Group.add_to_class('description', models.CharField(max_length=100, null=True))
Group.add_to_class('is_active', models.BooleanField(blank=True, null=True))
Group.add_to_class('created_at', models.DateTimeField(default=timezone.now))

User.add_to_class('pwd', models.CharField(max_length=100, null=True))
User.add_to_class('role', models.ForeignKey(Group, related_name='group', on_delete=models.CASCADE, null=True))
User.add_to_class('is_login', models.BooleanField(blank=True, null=True))

class UserProfile(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    login_time = models.DateTimeField(default=timezone.now)
    logout_time = models.DateTimeField(blank=True, null=True)
    duration = models.CharField(max_length=100, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "UserProfile"

