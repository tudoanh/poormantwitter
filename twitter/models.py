from django.db import models


class Tweet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=255)
    content = models.CharField(max_length=50)
