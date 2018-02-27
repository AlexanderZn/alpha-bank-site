from django.db import models
from django.utils import timezone
# Create your models here.


class Sphere_Company(models.Model):

    name = models.CharField(max_length=45)

    def __str__(self):
        return str(self.name)

class Company(models.Model):

    sphere = models.ForeignKey(Sphere_Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)

    def __str__(self):
        return str(self.name)

class Branch(models.Model):

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    info = models.CharField(max_length=100, default='Person')

    def __str__(self):
        return str(self.address)


class Subdivision(models.Model):

    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)

    def __str__(self):
        return str(self.name)


class Sphere_Person(models.Model):

    name = models.CharField(max_length=45)

    def __str__(self):
        return str(self.name)


class Specialization(models.Model):

    name = models.CharField(max_length=45)
    sphere = models.ForeignKey(Sphere_Person, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

class Person(models.Model):

    name = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    patronymic = models.CharField(max_length=45)
    male = models.BooleanField(default=1)
    age = models.IntegerField(default=18)
    phone = models.CharField(max_length=45)
    exp = models.IntegerField(default=0)
    salary = models.IntegerField(default=0)
    desiredSal = models.IntegerField(default=0)
    comments = models.CharField(max_length=100)

    def male_bool(self):
        if self.male == True:
            return 'М'
        else:
            return 'Ж'

    def __str__(self):
        return str(self.lastname) + str(self.name)


class Story(models.Model):

    subdivision = models.ForeignKey(Subdivision, on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date_update = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.person.lastname) + str(self.person.name) + \
               ":" + str(self.subdivision.branch.company.name)
