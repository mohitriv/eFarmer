from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
	path('', views.CropList.as_view(), name='AllCrops'),
	path('<int:pk>/', views.CropDetail.as_view(), name='CropWithId'),
	path('detail/<int:pk>/', views.getCropDetail, name='CropDetailWithId'),
	path('users/', views.UsersList.as_view(), name='AllUsers'),
	path('users/<int:pk>/', views.UsersDetail.as_view(), name='UserWithId'),
	#path('logout/', views.Logout.as_view(), name='Logout'),
]

urlpatterns = format_suffix_patterns(urlpatterns)