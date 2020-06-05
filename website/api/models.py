from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=100)
    war_name = models.CharField(max_length=30)
    number = models.IntegerField()

    class Meta:
        ordering = ['id']

class Word(models.Model):
    class Gender(models.TextChoices):
        DER = 'der'
        DIE = 'die'
        DAS = 'das'

    gender = models.CharField(choices=Gender.choices, max_length=100)
    word = models.CharField(max_length=100)
    translation = models.CharField(max_length=100, null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.gender + ' ' + self.word

class Dict(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)

    words = models.ManyToManyField(Word)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

