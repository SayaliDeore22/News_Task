from django.db import models


class Search(models.Model):
    keyword = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)