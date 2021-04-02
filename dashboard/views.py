from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

from college.models import Student, Staff

# Create your views here.
def index(request):
    return HttpResponse('Dashboard page')

# def authenticateViaEmail(user_email, password):
#     userModel = get_user_model()
#     try:
#         user = userModel.objects.get(useremail = user_email)
#     except Exception:
#         return None
    
#     if user.check_password(password):
#         return user
#     return None


def login(request):
    print(dict(request.session))
    if not request.session.__contains__('is_authenticated'): 
        print(request.POST)
        user_email = request.POST['useremail']
        password = request.POST['password']

        user_details = None
        # check for staff:
        try:
            user_details = Staff.objects.get(staff_email=user_email, staff_password = password)
            request.session['is_authenticated'] = True
            request.session['is_priviledged'] = True
            request.session['user_id'] = user_details.staff_id
        except Exception:
            user_details = None

        if user_details is None:
            #check for Student
            try:
                user_details = Student.objects.get(stud_email=user_email, stud_password = password)
                request.session['is_authenticated'] = True
                request.session['is_priviledged'] = True
                request.session['user_id'] = user_details.student_id
            except Exception:
                user_details = None

        if user_details is None:
            return HttpResponse('user not found')
        else:
            return HttpResponse('Logged In')
    else:
        return HttpResponse('You are already logged in')

def logout(request):
    if request.session.__contains__('is_authenticated'):
        del request.session['is_authenticated']
        del request.session['is_priviledged']
        del request.session['user_id']
        return HttpResponse('Logged out')
    else:
        return redirect('/events/AddEvents')

    
