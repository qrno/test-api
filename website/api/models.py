from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=100)
    war_name = models.CharField(max_length=30)
    number = models.IntegerField()

    class Meta:
        ordering = ['id']
