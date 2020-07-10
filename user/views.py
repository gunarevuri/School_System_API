from django.shortcuts import render
from django.http import JsonResponse
from .models import user

# Create your views here.
def index(request):
	context = {
	'users': user.objects.all()
	}
	return render(request, 'user/index.html',context)


def users_list(request):
	data = {
		'users':user.objects.all()
	}
	return JsonResponse(data)