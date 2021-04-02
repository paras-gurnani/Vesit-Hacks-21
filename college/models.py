
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
#     staff_id = models.AutoField(primary_key=True,default='')
#     # staff_email = models.CharField(max_length=100,unique=True)
#     # staff_fname = models.CharField(max_length=50)
#     # staff_lname = models.CharField(max_length=50)
    designation = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='college/staff/')
    phone_number = models.IntegerField()
    last_active = models.TimeField(auto_now=True)
    Staff_type = models.IntegerField()
    gender = models.TextField(max_length=1,default='')

    def __str__(self):
        return self.user.username


class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=25)
    dep_hod = models.ForeignKey(Staff,on_delete=models.CASCADE)
    # print(dep_hod)

    def __str__(self):
        return self.dept_name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # student_id=models.AutoField(primary_key=True)
    # stud_fname = models.CharField(max_length=50)
    # stud_lname = models.CharField(max_length=50)
    dept_id = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='department',default='')
    is_privileged = models.BooleanField(default=False)
    # stud_email = models.EmailField(default='')
    # stud_password = models.CharField(max_length=2000)
    stud_photo = models.ImageField(upload_to='college/student/')
    gender = models.CharField(max_length=1,default='')

    def __str__(self):
        return self.user.username

class Place(models.Model):
    place_id = models.AutoField(primary_key=True)
    place_name = models.CharField(max_length=50)
    capactiy = models.IntegerField()

    def __str__(self):
        return self.place_name

class Committee(models.Model):
    committee_id = models.AutoField(primary_key=True)
    comm_name = models.CharField(max_length=50)
    comm_level = models.CharField(max_length=30)
    comm_head = models.ForeignKey(Student,related_name='student',on_delete=models.CASCADE)

    def __str__(self):
        return self.comm_name


