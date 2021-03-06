from django.urls import path
from . import views

app_name='dashboard'

urlpatterns = [
    path('',views.index,name='index'),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('uploadProfilePic/', views.uploadProfilePic, name="upload_profile_pic")
]