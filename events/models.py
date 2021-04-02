from django.db import models
from college import models as mod
# Create your models here.
class Event(models.Model):

    event_title = models.CharField(max_length = 50, default="")
    event_description = models.CharField(max_length = 100)
    # event_start
    event_time = models.TimeField()
    event_date = models.DateField()
    # event_end
    end_time = models.TimeField()
    end_date = models.DateField()
    #organizer:
    is_student = models.BooleanField() # True: STUDENT, False: STAFF
    # registration_link
    registration_link = models.CharField(max_length = 100)
    # postor
    postor = models.ImageField(upload_to = 'Events/Postors', default="")
    #Foreign Keys

    event_place = models.ForeignKey(mod.Place, on_delete=models.CASCADE)


    dept_id = models.ForeignKey(mod.Department,on_delete=models.CASCADE,default=False)
    approval_id  = models.ForeignKey(mod.Staff,on_delete=models.CASCADE,default=False)
    event_type = models.IntegerField()
    #setting conductor id
    conductor_id=None
    if(is_student):
        conductor_id = models.ForeignKey(mod.Student,on_delete=models.CASCADE,default=False)
    else:
        conductor_id = models.ForeignKey(mod.Staff,on_delete=models.CASCADE,default=False)



