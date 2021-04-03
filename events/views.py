from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from college.models import *
from datetime import datetime,date,time


# Create your views here.
def index(request):
    context={}
    today = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    today_date,today_time = today.split(' ')
    hour,month,seconds = today_time.split(':')
    today_time = datetime.strptime(today_time,'%H:%M:%S').time()
    events = Event.objects.all().filter()
    today_date = date.today()
    # today_time= time.isoformat(timespec='auto')

    previous_events = Event.objects.all().filter(event_date__lt = today_date)
    upcoming_events = Event.objects.all().filter(event_date__gt = today_date)
    ongoing_events = Event.objects.all().filter(event_date__lte = today_date , end_date__gte = today_date)

    print(previous_events)
    print(upcoming_events)
    print(ongoing_events)
    context['events'] = upcoming_events
    return render(request,'events/allEvents.html',context=context)

def addEvent(request):
    places_object = Place.objects.all()
    places=[]
    context={}
    for place in places_object:
        places.append(place)
    print(places)
    context['places']=places

    return render(request, 'events/add_events.html',context=context)

def storeEvent(request):
    # print(request.POST)
    if(request.method == 'POST'):
        print(request.POST)
        event = Event()
        # Event details
        event.event_title = request.POST['title']
        event.event_description = request.POST['description']
        event.event_time = request.POST['start_time']
        event.event_date = request.POST['start_date']
        event.end_time = request.POST['end_time']
        event.end_date = request.POST['end_date']

        # organizer
        event.is_student=True
        is_student = request.POST['organizer']
        if(is_student == 1):
            event.is_student=False
            event.conductor_id = Staff.objects.get(staff_id = request.session['user_id'])
        else:
            event.conductor_id = Student.objects.get(student_id = request.session['user_id'])
        # if request.FILES['filename']:
        #     event.postor = request.FILES['filename']
        event.registration_link = request.POST['registration']
        place_name = request.POST['place']

        event.event_place = Place.objects.get(place_name=place_name)
        event.event_type = int(request.POST['level'])
        print(request.session['dept_id'])
        dept_id = int(request.session['dept_id'])
        dept_object = Department.objects.get(dept_id = dept_id)
        event.dept_id = dept_object
        event.status = 0
        event.save()




    return HttpResponse('Event Storage')

def eventDetail(request):
    return render(request, 'events/eventDetails.html')