from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import user
from rest_framework import status
from rest_framework.parsers import JSONParser
from user.serializers import userSerializer
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from rest_framework import generics

# Create your views here.
def index(request):
	context = {
	'users': user.objects.all()
	}
	return render(request, 'user/index.html',context)

@api_view(['GET', 'POST'])
def users_list(request):

	if request.method == 'GET':
		users = user.objects.all()
		serializer = userSerializer(users, many = True)
		# return JsonResponse(serializer.data, safe=False)

		#below response object return data in requested format
		return Response(serializer.data)


	if request.method == 'POST':
		# data = JSONParser().parse(request)
		serializer = userSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status = status.HTTP_201_CREATED)
		else:
			return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)




# @csrf_exempt
@api_view(['GET','PUT', 'POST', 'DELETE'])
def get_user(request, id):

	try:
		user_detail = user.objects.filter(user_id = id).first()
	except user.DoesNotExist:
		return Response(status= status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = userSerializer(user_detail)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = userSerializer(user_detail, data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		user_detail.delete()
		return Response(status= status.HTTP_204_NO_CONTENT)

#####----------We can also use class based views to List , update, delete user from DB (CRUD)-------------------##


class UserList(generics.ListAPIView):
	queryset = user.objects.all()
	serializer_class = userSerializer

class UserCreate(generics.CreateAPIView):
	serializer_class = userSerializer

	def create(self, request, *args, **kwargs):
		try:
			first_name = request.data.get('first_name')
			last_name = request.data.get('last_name')
			phone_number = request.data.get('phone_number')

			if first_name is None or last_name is None or phone_number is None:
				raise ValidationError({'last_name and first_name and phone_number':'must be included'})
		except Exception as e:
			print(e)
		return super().create(request, *args, **kwargs)


class UserRetrieve(generics.RetrieveAPIView):
	serializer_class = userSerializer
	queryset = user.objects.all()
	lookup_field = 'user_id'

	def Retrieve(self,request, *args, **kwargs):
		user_detail = request.data.get('user_id')
		response = super().retrieve(request , *args, **kwargs)
		return response

class UserDestroy(generics.DestroyAPIView):
	serializer_class = userSerializer
	queryset = user.objects.all()
	lookup_field = 'user_id'

	def delete(self,request, *args, **kwargs):
		user_detail = request.data.get('user_id')
		respone = super().delete(request , *args, **kwargs)
		return respone

class UserUpdate(generics.UpdateAPIView):
	serializer_class = userSerializer
	queryset = user.objects.all()
	lookup_field = 'user_id'

	def Retrieve(self,request, *args, **kwargs):
		user_detail = request.data.get('user_id')
		response = super().retrieve(request , *args, **kwargs)
		return response

	def update(self, request, *args, **kwargs):
		user_detail = request.data.get('user_id')
		response = super().update(request, *args, **kwargs)
		return response










