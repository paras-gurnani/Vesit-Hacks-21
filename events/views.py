from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Events page')

def addEvent(request):
    return render(request, 'events/add_events.html')

def storeEvent(request):
    print(request.POST)
    return HttpResponse('Event Storage')