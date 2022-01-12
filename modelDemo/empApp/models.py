from django.db import models


class Employee(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    salary = models.FloatField()
    email = models.EmailField(max_length=30)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'


class Programmer(models.Model):
    name = models.CharField(max_length=30)
    sal = models.IntegerField()


class Project(models.Model):
    name = models.CharField(max_length=30)
    programmers = models.ManyToManyField(Programmer)


class Customer(models.Model):
    name = models.CharField(max_length=30)


class PhoneNumber(models.Model):
    type = models.CharField(max_length=10)
    number = models.CharField(max_length=10)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Person(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    age = models.IntegerField()


class License(models.Model):
    type = models.CharField(max_length=10)
    validFrom = models.DateField()
    validTo = models.DateField()
    age = models.IntegerField()
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
