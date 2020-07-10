from django.shortcuts import render
from .models import user

# Create your views here.
def index(request):
	context = {
	'users': user.objects.all()
	}
	return render(request, 'user/index.html',context)