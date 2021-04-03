from django.shortcuts import render, redirect
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
    upcoming_events = Event.objects.all().filter(event_date__gt = today_date,status=1)
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
        event.status = 0
        event.save()

    return redirect('/events')

def eventDetail(request, id):
    today_date = date.today()
    event = Event.objects.get(id=id)
    context = {
        'event_title': event.event_title,
        'event_description': event.event_description,
        'registration_link': event.registration_link,
        'start_date' : event.event_date,
        'start_time' : event.event_time,
        'end_date' : event.end_date,
        'end_time' : event.end_time,
        'event_place' : event.event_place,
        'event_postor': event.postor,
        'is_this_previous': True if event.event_date < today_date else False
    }
    print(context)
    return render(request, 'events/eventDetails.html', context)


  

def previousEvents(request):
    context = {}
    today_date = date.today()
    previous_events = Event.objects.all().filter(event_date__lt=today_date,status=1)
    context['events'] = previous_events
    return render(request,'events/previousEvents.html',context=context)

def onGoingEvents(request):
    context={}
    today_date = date.today()
    ongoing_events = Event.objects.all().filter(event_date__lte=today_date, end_date__gte=today_date,status=1)
    context['events']=ongoing_events
    return render(request,'events/ongoing.html',context=context)

    
def approveEvent(request):
    # status: 0 ---> Pending
    # status: 1 ---> Accept
    # status: 2 ---> Rejected
    staff_type = request.session['Staff_type']
    context = {}
    print('--------------', staff_type)
    if staff_type > 0:
        if staff_type == 3:
            pending_approvals = Event.objects.all().filter(status=0, event_type = staff_type)
            accepted_approvals = Event.objects.all().filter(status=1, event_type = staff_type)
            rejected_approvals = Event.objects.all().filter(status=2, event_type = staff_type)
            context = {
                        'pending_approvals': pending_approvals,
                        'accepted_approvals': accepted_approvals,
                        'rejected_approvals': rejected_approvals
                        }
        else:
            dept_object = Department.objects.get(dept_id = request.session['dept_id'])
            pending_approvals = Event.objects.all().filter(status=0, event_type = staff_type, dept_id = dept_object)
            accepted_approvals = Event.objects.all().filter(status=1, event_type = staff_type, dept_id = dept_object)
            rejected_approvals = Event.objects.all().filter(status=2, event_type = staff_type, dept_id = dept_object)
            context = {
                        'pending_approvals': pending_approvals,
                        'accepted_approvals': accepted_approvals,
                        'rejected_approvals': rejected_approvals
                        }

    return render(request, 'events/give_approval.html', context)

def approve(request, id):
    print('Approval ---- ', id)
    event_object = Event.objects.get(id=id, status=0)
    event_object.status = 1

    user_id = request.session['user_id']
    event_object.approval_id = Staff.objects.get(staff_id = user_id)
    event_object.save(update_fields = ['status', 'approval_id'])
    return redirect('/events/ApproveEvent')

def reject(request, id):
    print('Approval ---- ', id)
    event_object = Event.objects.get(id=id, status=0)
    event_object.status = 2

    user_id = request.session['user_id']
    event_object.approval_id = Staff.objects.get(staff_id = user_id)
    event_object.save(update_fields = ['status', 'approval_id'])
    return redirect('/events/ApproveEvent')
