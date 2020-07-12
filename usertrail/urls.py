"""usertrail URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.urls import include, path
	2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import user.views as user_views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', user_views.index, name='index'),
	path('v1/users/', user_views.users_list, name='userslist'),
	path('v1/users/<int:id>/', user_views.get_user, name='userdetails'),
	path('v1/users/submissions/<int:id>/', user_views.get_user_submissions, name='get_user_submissions'),
	path('v1/users/submissions/', user_views.get_all_submissions, name='get_all_submissions'),



	path('class/v1/users/', user_views.UserList.as_view(), name='classuserlist'),
	path('class/v1/users/<int:user_id>/', user_views.UserRetrieve.as_view(), name='classretrieve'),
	path('class/v1/users/delete/<int:user_id>/', user_views.UserDestroy.as_view(), name='classdestroy'),
	path('class/v1/users/create/', user_views.UserCreate.as_view(), name='usercreate'),
	path('class/v1/users/<int:user_id>/update/', user_views.UserUpdate.as_view(), name='classupdate'),
]

# urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

