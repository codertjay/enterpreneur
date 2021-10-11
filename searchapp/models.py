from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class SearchQuery(models.Model):
    user = models.ForeignKey(User, blank=True, null=True,on_delete=models.SET_NULL)
    query = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
