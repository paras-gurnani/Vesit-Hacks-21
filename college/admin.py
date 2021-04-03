from django.contrib import admin

from .models import Staff, Department, Student, Place, Committee,StudentInCommittees
# Register your models here.

admin.site.register(Staff)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Place)
admin.site.register(Committee)
admin.site.register(StudentInCommittees)

