from django.db import models
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=200, default="")
    pub_date = models.DateTimeField(default=datetime.now)
    text = models.TextField(default="")
