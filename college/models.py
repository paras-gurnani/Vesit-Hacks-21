from django.db import models

# Create your models here.
class Staff(models.Model):

    staff_id = models.AutoField(primary_key=True,default='')
    staff_email = models.CharField(max_length=100,unique=True)
    staff_fname = models.CharField(max_length=50)
    staff_lname = models.CharField(max_length=50)
    designation = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='staff/')
    phone_number = models.IntegerField()
    last_active = models.TimeField(auto_now=True)
    type = models.IntegerField()
    gender = models.TextField(max_length=1,default='')


class Department(models.Model):
    dept_id = models.AutoField(primary_key=True,default='')
    dept_name = models.CharField(max_length=25)
    dep_hod = models.ForeignKey(Staff,on_delete=models.CASCADE,related_name='staff')

class Student(models.Model):

    student_id=models.AutoField(primary_key=True)
    stud_fname = models.CharField(max_length=50)
    stud_lname = models.CharField(max_length=50)
    dept_id = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='department',default='')
    is_privileged = models.BooleanField(default=False)
    stud_email = models.EmailField(default='')
    stud_password = models.CharField(max_length=2000)
    stud_photo = models.ImageField(upload_to='student/')
    gender = models.CharField(max_length=1,default='')

class Place(models.Model):
    place_id = models.AutoField(primary_key=True)
    place_name = models.CharField(max_length=50)
    capactiy = models.IntegerField()




