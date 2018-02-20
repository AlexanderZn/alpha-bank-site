from django.db import models
from django.utils import timezone
# Create your models here.


class Sphere_Company(models.Model):

    name = models.CharField(max_length=45)


class Company(models.Model):

    id_Sphere = models.ForeignKey(Sphere_Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)


class Branch(models.Model):

    id_Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    info = models.CharField(max_length=100, default='Person')


class Subdivision(models.Model):

    id_Branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)


class Sphere_Person(models.Model):

    name = models.CharField(max_length=45)


class Person(models.Model):

    name = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    patronymic_Person = models.CharField(max_length=45)
    male = models.BooleanField(default=1)
    age = models.IntegerField(default=18)
    phone = models.CharField(max_length=45)
    exp = models.IntegerField(default=0)
    salary = models.IntegerField(default=0)
    desiredSal = models.IntegerField(default=0)
    comments = models.CharField(max_length=100)

    def male_bool(self):
        return str(self.male)


class Story(models.Model):

    id_Subdivision = models.ForeignKey(Subdivision, on_delete=models.CASCADE)
    id_Sphere = models.ForeignKey(Sphere_Person, on_delete=models.CASCADE)
    id_Person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date_update = models.DateTimeField(default=timezone.now())


