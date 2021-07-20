from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=60)
    rating = models.IntegerField()