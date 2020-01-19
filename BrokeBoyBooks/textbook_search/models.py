from django.db import models

# Create your models here.

class Textbook(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=75)
    edition = models.IntegerField()
    link = models.CharField(max_length=200)

