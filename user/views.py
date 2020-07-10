from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import user
from rest_framework import status
from rest_framework.parsers import JSONParser
from user.serializers import userSerializer
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response



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





# def submit_assignment():







