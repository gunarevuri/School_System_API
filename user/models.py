from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

status_field = ['actice','inactive']
enroll_status = ['enrolled','not_enrolled']
class_subjects = ['maths','science','social','phisics']
homework_resource_type=['video','image','file','text']
correction_resource_type= ['video', 'image', 'file', 'text']
submissions_resource_type = ['video', 'image', 'file', 'text']

class user(models.Model):
	user_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=255, )
	last_name = models.CharField(max_length=255, )
	phone_number = PhoneNumberField(blank=False)
	status = models.CharField(choices=[(x,x) for x in status_field], max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '{} {} and {}'.format(self.user_id,self.first_name,self.last_name)


class School(models.Model):
	school_id = models.AutoField(primary_key = True)
	school_name = models.CharField(max_length=255)
	user_id = models.ForeignKey(user, on_delete=models.CASCADE)
	state_id = models.IntegerField()
	city_id = models.IntegerField()
	contact_number = PhoneNumberField(blank=True)
	photo = models.ImageField(upload_to ='schoolimages/school_photos/',max_length=250,height_field=None,width_field=None)
	rural = models.BooleanField()
	district = models.CharField(max_length=255)
	block = models.CharField(max_length=255)
	cluster = models.CharField(max_length=255)
	village = models.CharField(max_length=255)
	zipcode = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return 'school_id {} and school_name{}'.format(self.school_id, self.school_name)

class userPersona(models.Model):
	user_id = models.ForeignKey(user, on_delete=models.CASCADE)
	# user_persona = models.CharField(choices=[(x,x) for x in user_persona_field])
	status = models.CharField(choices=[(x,x) for x in status_field], max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Parent(models.Model):
	user_id = models.ForeignKey(user, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '{} {}'.format(self.user_id.first_name,self.user_id.last_name)

class Student(models.Model):
	student_id = models.AutoField(primary_key = True)
	student_name = models.CharField(max_length=50)
	school_id = models.ForeignKey(School, on_delete=models.CASCADE)
	parent_id = models.ForeignKey(Parent, on_delete=models.CASCADE)
	roll_number = models.IntegerField()
	gender = models.CharField(choices=[('M','Male'),('F','Female'),('not interested','not interested')], max_length=100)
	status = models.CharField(choices=[(x,x) for x in status_field],max_length=50)
	year_of_birth= models.IntegerField()
	photo = models.ImageField(upload_to ='Student/student_photos/',max_length=250,height_field=None,width_field=None)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.student_name


class Teacher(models.Model):
	teacher_id = models.AutoField(primary_key=True)
	user_id = models.ForeignKey(user, on_delete=models.CASCADE)
	school_id = models.ForeignKey(School, on_delete=models.CASCADE)
	gender = models.CharField(choices=[('M','Male'),('F','Female'),('not interested','not interested')], max_length=100)
	year_of_birth= models.IntegerField()
	photo = models.ImageField(upload_to ='Teacher/teacher_photos/',max_length=250,height_field=None,width_field=None)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class Board(models.Model):
	board_id = models.AutoField(primary_key=True)
	board_name = models.CharField(max_length=255)
	is_state_board = models.BooleanField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class School_Board_Bridge(models.Model):
	school_id = models.IntegerField()
	board_id = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		unique_together = [('school_id','board_id'),]




class State(models.Model):
	state_id = models.AutoField(primary_key = True)
	state_name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class Class(models.Model):
	class_id = models.AutoField( primary_key = True)
	grade = models.IntegerField()
	section = models.CharField(max_length=255)
	school_id = models.ForeignKey(School, on_delete=models.CASCADE)
	academic_year = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return 'class Grade {} and Section {}'.format(self.grade, self.section)

class ClassSubjects(models.Model):
	class_subject_id = models.AutoField(primary_key=True)
	class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
	subject = models.CharField(choices=[(x,x) for x in class_subjects], max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return ' class Grade {}'.format(self.class_id.grade)

class Homework(models.Model):
	homework_id = models.AutoField(primary_key = True)
	class_subject_id = models.ForeignKey(ClassSubjects, on_delete = models.CASCADE)
	teacher_id = models.ForeignKey(Teacher, on_delete = models.CASCADE)
	due_data = models.DateTimeField()
	marks_total = models.DecimalField(max_digits=5,decimal_places=2)
	released_status = models.CharField(choices=[(x,x) for x in status_field], max_length=50)
	released_on = models.DateTimeField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return 'home work for{0}  from Teacher {1} {2}'.format(self.class_subject_id.class_id.grade, self.teacher_id.user_id.first_name, self.teacher_id.user_id.last_name)

class Submissions(models.Model):
	submission_id = models.AutoField(primary_key = True)
	homework_id = models.ForeignKey(Homework, on_delete = models.CASCADE)
	student_id = models.ForeignKey(Student, on_delete = models.CASCADE)
	submitted_data = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)	


class ClassEnrollment(models.Model):
	student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
	class_id = models.ForeignKey(Class, on_delete=models.CASCADE )
	enrollment_status = models.CharField(choices=[(x,x) for x in enroll_status], max_length=50,  null=True,blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		unique_together = (('student_id', 'class_id'),)


class SubmissionResources(models.Model):
	submissions_resource_id = models.AutoField(primary_key=True)
	submission_id = models.ForeignKey(Submissions, on_delete = models.CASCADE)
	resource_type = models.CharField(choices=[(x,x) for x in submissions_resource_type], max_length= 500, null=True,blank=True)

	resource_image = models.ImageField(upload_to='SubmissionResources/', verbose_name="Image Resource (optional)", null=True,blank=True)
	resource_video = models.FileField(upload_to='SubmissionResources/' ,verbose_name="Video Resouce (optional)", null=True,blank=True)
	resource_File = models.FileField(upload_to='SubmissionResources/', verbose_name="File Resouce (optional)", null=True,blank=True)

	resource_link = models.URLField( max_length=500, )
	caption = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '{} resource_link {}'.format(self.submission_id.student_id.student_name, self.resource_link)

class Corrections(models.Model):
	correction_id = models.AutoField(primary_key = True)
	submissions_id = models.ForeignKey(Submissions, on_delete = models.CASCADE)
	marks_received = models.DecimalField(max_digits=5, decimal_places=2)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class CorrectionsResources(models.Model):
	correction_resource_id = models.AutoField(primary_key=True)
	correction_id = models.ForeignKey(Corrections, on_delete = models.CASCADE)
	resource_type = models.CharField(choices=[(x,x) for x in correction_resource_type], max_length=200, null=True,blank=True)
	resource_image = models.ImageField(upload_to='correction_resources/', verbose_name="Image Resource (optional)", null=True,blank=True)
	resource_video = models.FileField(upload_to='correction_resources/', verbose_name='Video Resouce (optional)', null=True,blank=True)
	resource_File = models.FileField(upload_to='correction_resources/' ,verbose_name='File Resouce (optional)', null=True,blank=True)

	resource_link = models.URLField(max_length= 500,null=True, blank=True, )
	caption = models.CharField(max_length= 255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class HomeworkResources(models.Model):

	homework_resource_id = models.AutoField( primary_key = True)
	homework_id = models.ForeignKey(Homework, on_delete = models.CASCADE)
	resource_type = models.CharField(choices=[(x,x) for x in homework_resource_type], max_length=200, null=True,blank=True)
	resource_image = models.ImageField(upload_to='HomeworkResources/%m/%d/', verbose_name="Image Resource (optional)", null=True,blank=True)
	resource_video = models.FileField(upload_to='HomeworkResources/%m/%d/', verbose_name='Video Resouce (optional)', null=True,blank=True)
	resource_File = models.FileField(upload_to='HomeworkResources/%m/%d/' ,verbose_name='File Resouce (optional)', null=True,blank=True)
	file_field = models.FileField(upload_to='HomeworkResources/%m/%d/', null=True,blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)












