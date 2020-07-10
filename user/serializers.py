from rest_framework import serializers
from user.models import *

class userSerializer(serializers.ModelSerializer):
	class Meta:
		model = user
		fields = ['user_id', 'first_name', 'last_name' , 'phone_number', 'status', 'created_at','updated_at']

