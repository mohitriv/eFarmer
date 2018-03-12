from django.urls import path

from . import views

urlpatterns = [
	path('', views.getCrops, name='AllCrops'),
	path('<int:cropId>/', views.getCropWithId, name='CropWithId'),
	path('detail/<int:cropId>/', views.getCropDetail, name='CropDetailWithId'),
	path('users/', views.getUsers, name='AllUsers'),
	path('users/<int:userId>/', views.getUserWithId, name='UserWithId'),
]