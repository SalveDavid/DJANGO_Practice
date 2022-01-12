from django.db import models


class Patient(models.Model):
    lastName = models.CharField(max_length=20)
    firstName = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.firstName} {self.lastName}'


class ClinicalData(models.Model):
    COMPONENT_NAMES = [('hw', 'Height/Weight'), ('bp', 'Blood Pressure'), ('heartrate', 'Heart Rate')]
    componentName = models.CharField(choices=COMPONENT_NAMES, max_length=20)
    componentValue = models.CharField(max_length=20)
    measuredDateTime = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

