from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from college.models import *
from datetime import datetime


# Create your views here.
def index(request):
    return HttpResponse('Events page')

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
        title = request.POST['title']
        description = request.POST['description']
        start_date = datetime.strptime(request.POST['start_date'], '%Y-%m-%d')
        start_time = datetime.strptime(request.POST['start_time'], '%I:%M')
        print(start_date, type(start_date))
        print(start_time)
        # event = Event()
        # event.event_title = request.POST['title']
        # event.event_description = request.POST['description']
        # event.event_time = request.POST['start_time']
        # event.event_date = request.POST['start_date']
        # event.end_time = request.POST['end_time']
        # event.end_date = request.POST['end_date']
        # event.is_student=True
        # is_student = request.POST['organizer']
        # if(is_student == 1):
        #     event.is_student=False
        # event.postor = request.FILES['filename']
        # event.registration_link = request.POST['registration']


        # place_name = request.POST['place']
        # # print(Place.objects.get(place_name=place_name))
        # event.event_place = Place.objects.get(place_name=place_name)


        # event.event_type = int(request.POST['level'])
        # event.save()




    return HttpResponse('Event Storage')

def eventDetail(request):
    return render(request, 'events/eventDetails.html')