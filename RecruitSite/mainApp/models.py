from django.db import models

# Create your models here.


class Sphere_Company(models.Model):

    name = models.CharField(max_length=45)


class Company(models.Model):

    sphere = models.ForeignKey(Sphere_Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)


class Branch(models.Model):

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)


class Subdivision(models.Model):

    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)


class Sphere_Person(models.Model):

    name = models.CharField(max_length=45)


class Person(models.Model):

    name = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    patronymic_person = models.CharField(max_length=45)
    male = models.BooleanField(default=1)
    age = models.IntegerField(default=18)
    phone = models.CharField(max_length=45)
    experience = models.IntegerField(default=0)
    salary = models.IntegerField(default=0)
    desiredSal = models.IntegerField(default=0)
    comments = models.CharField(max_length=100)

    def male_bool(self):
        return str(self.gender)


class Story(models.Model):

    subdivision = models.ForeignKey(Subdivision, on_delete=models.CASCADE)
    sphere = models.ForeignKey(Sphere_Person, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date_update = models.DateTimeField


