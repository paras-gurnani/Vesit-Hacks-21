from django.contrib import admin

<<<<<<< HEAD
from .models import Staff, Department, Student, Place, Committee,StudentInCommittees
=======
from .models import Staff, Department, Student, Place, Committee
>>>>>>> dfc9d7cf57d4246a66b3b8c8b3325d099a17913b
# Register your models here.

admin.site.register(Staff)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Place)
admin.site.register(Committee)
<<<<<<< HEAD
admin.site.register(StudentInCommittees)
=======
>>>>>>> dfc9d7cf57d4246a66b3b8c8b3325d099a17913b

