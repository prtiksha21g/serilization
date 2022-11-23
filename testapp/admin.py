from django.contrib import admin
from testapp.models import Student

# Register your models here.
#@admin.register(Student) #...we can aslo register like this
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','rollno','city']

admin.site.register(Student,StudentAdmin)