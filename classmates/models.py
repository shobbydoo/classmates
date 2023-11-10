from django.db import models

# Create your models here.

from django.db import models
from django.urls import reverse

class Classmate(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    age = models.IntegerField()
    address = models.EmailField(blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.firstname

    def get_absolute_url(self):
        return reverse('classmate_edit', kwargs={'pk': self.pk})
