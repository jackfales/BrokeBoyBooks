from django.db import models

# Create your models here.

class Textbook(models.Model):
    #auto_increment_id = models.AutoField(editable=False, primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=75)
    edition = models.IntegerField()
    link = models.CharField(max_length=200)

