from venv import create
from django.db import models

class  Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.CharField(max_length=150, default="anonymus")
    created = models.DateTimeField(auto_now_add=True)
