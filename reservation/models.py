from django.db import models

# Create your models here.

class Reservation(models.Model):

    name = models.CharField(max_length=30)
    email = models.EmailField()
    Phone = models.IntegerField()
    number_of_person = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    message = models.CharField(max_length=300)

    def __str__(self):
        return self.name

        