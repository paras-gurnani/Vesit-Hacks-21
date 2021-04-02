from django.db import models

# Create your models here.
class Event(models.Model):
    event_description = models.CharField(max_length = 100)
    # event_start
    event_time = models.TimeField()
    event_date = models.DateField()
    # event_end
    end_time = models.TimeField()
    end_date = models.DateField()
    #organizer:
    is_student_or_staff = models.BooleanField() # True: STUDENT, False: STAFF
    # registration_link
    registration_link = models.CharField(max_length = 100)
    # postor
    postor = models.ImageField(upload_to = 'Events/Postors', default="")
    
