from django.contrib import admin

# Register your models here.
from .models import user, School, userPersona, Student,Parent,Teacher, State, Class, ClassSubjects, Homework, Submissions, ClassEnrollment,CorrectionsResources,Corrections,SubmissionResources,HomeworkResources, Board,School_Board_Bridge

admin.site.register(user)

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
	list_display = ('school_id', 'school_name','contact_number', 'created_at','updated_at')

admin.site.register(userPersona)
admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Teacher)
admin.site.register(State)
admin.site.register(Class)
admin.site.register(ClassSubjects)
admin.site.register(ClassEnrollment)
admin.site.register(Homework)
admin.site.register(Submissions)
admin.site.register(School_Board_Bridge)
admin.site.register(Board)
admin.site.register(HomeworkResources)
admin.site.register(SubmissionResources)
admin.site.register(Corrections)
admin.site.register(CorrectionsResources)