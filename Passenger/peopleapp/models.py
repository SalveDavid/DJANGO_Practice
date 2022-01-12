from django.db import models


class Passenger(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    rewardPoints = models.IntegerField()

    def __str__(self):
        return f'{self.firstName} {self.lastName}'
