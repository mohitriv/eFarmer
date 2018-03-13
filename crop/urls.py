from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
	path('', views.getCrops, name='AllCrops'),
	path('<int:cropId>/', views.getCropWithId, name='CropWithId'),
	path('detail/<int:cropId>/', views.getCropDetail, name='CropDetailWithId'),
	path('users/', views.UsersList.as_view(), name='AllUsers'),
	path('users/<int:pk>/', views.UsersDetail.as_view(), name='UserWithId'),
]

urlpatterns = format_suffix_patterns(urlpatterns)