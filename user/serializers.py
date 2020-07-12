from rest_framework import serializers
from user.models import *

class userSerializer(serializers.ModelSerializer):
	class Meta:
		model = user
		fields = ['user_id', 'first_name', 'last_name' , 'phone_number', 'status', 'created_at','updated_at']


class SubmissionsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Submissions
		fields = ['submission_id', 'homework_id', 'student_id', 'submitted_data']


class SubmissionResourcesSerializer(serializers.ModelSerializer):
	class Meta:
		model = SubmissionResources
		fields = ['submissions_resource_id', 'submission_id', 'resource_type','resource_image','resource_video','resource_File','resource_link' ,'caption']

