from django.db import models

# Create your models here.


class School(models.Model):
    name =  models.CharField(max_length=20)
    max_student = models.IntegerField(default=100000)

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    id_string = models.CharField(max_length=20)
    school = models.ForeignKey(School, on_delete=models.CASCADE, default=1)

