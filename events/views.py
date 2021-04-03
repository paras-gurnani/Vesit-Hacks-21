from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Event
from college.models import *


# Create your views here.
def index(request):
    context={}
    events = Event.objects.all()
    for event in events:
        print(event.event_description)
        print(event.postor)
    context['events'] = events
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
        if request.FILES['filename']:
            event.postor = request.FILES['filename']
        event.registration_link = request.POST['registration']
        place_name = request.POST['place']

        event.event_place = Place.objects.get(place_name=place_name)
        event.event_type = int(request.POST['level'])
        print(request.session['dept_id'])
        dept_id = int(request.session['dept_id'])
        dept_object = Department.objects.get(dept_id = dept_id)
        event.dept_id = dept_object
        event.save()

    return redirect('/events')

def eventDetail(request, id):
    event = Event.objects.get(id=id)
    context = {
        'event_title': event.event_title,
        'event_description': event.event_description,
        'registration_link': event.registration_link,
        'event_postor': event.postor
    }
    print(context)
    return render(request, 'events/eventDetails.html', context)

def approveEvent(request):
    return render(request, 'events/give_approval.html')