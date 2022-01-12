from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=20)
    instructor = models.CharField(max_length=20)
    rating = models.IntegerField()
