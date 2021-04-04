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
            request.session['user_email'] = user_details.staff_email
            request.session['user_fname'] = user_details.staff_fname
            request.session['dept_id'] = user_details.dept_id.dept_id
            request.session['Staff_type'] = user_details.Staff_type
            request.session['is_student'] = False
        except Exception:
            user_details = None

        if user_details is None:
            #check for Student
            try:
                user_details = Student.objects.get(stud_email=user_email, stud_password = password)
                request.session['is_authenticated'] = True
                request.session['is_priviledged'] = True
                request.session['user_id'] = user_details.student_id
                request.session['user_email'] = user_details.stud_email
                request.session['user_fname'] = user_details.stud_fname
                request.session['dept_id'] = user_details.dept_id.dept_id
                request.session['Staff_type'] = 0 # for student
                request.session['is_student'] = True
            except Exception:
                user_details = None

        if user_details is None:
            return HttpResponse('user not found')
        else:
            return redirect('/events')
    else:
        return HttpResponse('You are already logged in')

def logout(request):
    print(dict(request.session))
    if request.session.__contains__('is_authenticated'):
        del request.session['is_authenticated']
        del request.session['is_priviledged']
        del request.session['user_id']
        del request.session['user_email']
        del request.session['user_fname']
        del request.session['dept_id']
        del request.session['Staff_type']
        del request.session['is_student']
        return redirect('/events')
    else:
        return render(request, '/events/add_events.html')

def profile(request):
    user_id = request.session['user_id']
    if request.session['is_student']:
        student_object = Student.objects.get(student_id = user_id)
        context = {
            'name': student_object.stud_fname + ' ' + student_object.stud_lname,
            'email': student_object.stud_email,
            'department': student_object.dept_id.dept_name,
            'Designation': 'Student',
            'Photo': student_object.stud_photo
        }
    else:
        staff_object = Staff.objects.get(staff_id = user_id)
        context = {
            'name': staff_object.staff_fname + ' ' + staff_object.staff_lname,
            'email': staff_object.staff_email,
            'department': staff_object.dept_id.dept_name,
            'Designation': staff_object.designation,
            'Photo': staff_object.photo
        }
    print(context)
    return render(request, 'dashboard/profile.html', context)

def uploadProfilePic(request):
    print(request.FILES['photos'])
    user_object = None
    if request.session['is_student']:
        user_object = Student.objects.get(student_id = request.session['user_id'])
        user_object.stud_photo = request.FILES['photos']
        user_object.save(update_fields=['stud_photo'])
    else:
        user_object = Staff.objects.get(staff_id = request.session['user_id'])
        user_object.photo = request.FILES['photos'] 
        user_object.save(update_fields=['photo'])
    
    return redirect('/dashboard/profile')
    
