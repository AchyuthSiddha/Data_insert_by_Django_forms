from django.db import models

# Create your models here.

class Student(models.Model):
    sid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    mobile=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.name
    

class Course(models.Model):
    cid=models.IntegerField()
    sid=models.ForeignKey(Student,on_delete=models.CASCADE)
    cname=models.CharField(max_length=100)
    Ctrianer=models.CharField(max_length=100)

    def __str__(self):
        return self.cname
