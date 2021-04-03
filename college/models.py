from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=25)


    def __str__(self):
        return self.dept_name


class Staff(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_id = models.AutoField(primary_key=True)
    staff_email = models.CharField(max_length=100, unique=True, default='')
    staff_password = models.CharField(max_length=200, default='')
    staff_fname = models.CharField(max_length=50, default='')
    staff_lname = models.CharField(max_length=50, default='')
    designation = models.CharField(max_length=20, default='')
    photo = models.ImageField(upload_to='college/staff/', null=True, blank=True)
    phone_number = models.IntegerField()

    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='staff_dept_id', null=True,
                                blank=True)

    dept_id = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='staff_dept_id',null=True,blank=True)

    last_active = models.TimeField(auto_now=True)
    Staff_type = models.IntegerField()
    gender = models.TextField(max_length=1, default='')

    def __str__(self):
        return self.staff_fname



class Student(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.AutoField(primary_key=True)
    stud_fname = models.CharField(max_length=50)
    stud_lname = models.CharField(max_length=50)
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department', default='')
    is_privileged = models.BooleanField(default=False)
    stud_email = models.EmailField(default='')
    stud_password = models.CharField(max_length=2000)
    stud_photo = models.ImageField(upload_to='college/student/', null=True, blank=True)
    gender = models.CharField(max_length=1, default='')

    def __str__(self):
        return self.stud_email


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
    comm_head = models.ForeignKey(Student, related_name='student', on_delete=models.CASCADE)

    def __str__(self):
<<<<<<< HEAD
        return self.comm_name

class StudentInCommittees(models.Model):
    student = models.ForeignKey(Student,  on_delete=models.CASCADE)
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.stud_fname
    

=======
        return self.comm_name
>>>>>>> dfc9d7cf57d4246a66b3b8c8b3325d099a17913b
