from django.urls import path
from . import views

app_name='events'

urlpatterns = [
    path('', views.index,name='index'),
    path('AddEvent/', views.addEvent, name='add_event'),
    path('StoreEvent/', views.storeEvent, name='store_event')
]