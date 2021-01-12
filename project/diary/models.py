from django.db import models
from django.utils import timezone

# Create your models here.

class Day(models.Model):
    # id = models.AutoField(primary_key=True) 内部で自動に起こる
    title = models.CharField("Title", max_length=200)
    text = models.TextField("Main content")
    date = models.DateTimeField("Day", default=timezone.now)

