from django.db import models


# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    username=models.CharField(max_length=35)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    confirm_password=models.CharField(max_length=50)

    def __str__(self):
        return self.first_name


class Class(models.Model):
    sid = models.CharField(max_length=25)
    name=models.CharField(max_length=40)
    subject = models.CharField(max_length=40)
    sec = models.CharField(max_length=50)

    def __str__(self):
        return self.name


