from django.http import HttpResponse, JsonResponse

from django.shortcuts import get_object_or_404

from .models import Crop, CropDetail, User, Seller, Buyer, Order

from .serializers import CropSerializer, CropDetailSerializer, UserSerializer, SellerSerializer, BuyerSerializer

from rest_framework.views import APIView

from rest_framework.response import Response

from django.http import Http404

from rest_framework import status 

from .permissions import UserEndpointPermission

from rest_framework.parsers import JSONParser

# Create your views here.

'''
Crops methods
'''
# Get all Crops

class CropList(APIView):
	def get(self, request, format=None):
		category = request.GET.get('category')
		if category is None: # /crop/
			# Fetch all the crops and return the Crop objects
			crops = Crop.objects.all()
			cropSerializer = CropSerializer(crops, many=True)
			return JsonResponse(cropSerializer.data, safe=False)
		else: # /crop/catogory=Rice
			crops = Crop.objects.filter(category__icontains=category)
			cropSerializer = CropSerializer(crops, many=True)
			return JsonResponse(cropSerializer.data, safe=False)	

class CropDetailWithId(APIView):
	def get(self, request, pk, format=None):
		crop = get_object_or_404(Crop, pk=pk)
		cropSerializer = CropSerializer(crop)
		return JsonResponse(cropSerializer.data)

class CropMetaDetail(APIView):
	def get(self, request, pk, format=None):
		cropDetail = get_object_or_404(CropDetail, crop__id=pk)
		cropDetailSerializer = CropDetailSerializer(cropDetail)
		return JsonResponse(cropDetailSerializer.data)

'''
Users methods
'''
class UsersList(APIView):
	
	#parser_classes = (JSONParser,)
	permission_classes = (UserEndpointPermission,)

	def getObject(self, pk):
		try:
			return User.objects.get(pk=pk)
		except:
			raise Http404

	def get(self, request, format=None):
		pk = request.user.id
		user = self.getObject(pk)
		serializer = UserSerializer(user)
		return Response(serializer.data)
   
	def post(self, request, format=None):
		if 'category' in request.data and request.data['category'].lower() == "Seller".lower():
			serializer = SellerSerializer(data=request.data)
		else:
			serializer = BuyerSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsersDetail(APIView):

	def getObject(self, pk):
		try:
			return User.objects.get(pk=pk)
		except:
			raise Http404

	def get(self, request, pk, format=None):
		user = self.getObject(pk)
		serializer = UserSerializer(user)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		user = self.getObject(pk)
		serializer = UserSerializer(user, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		user = self.getObject(pk)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class Logout(APIView):

	def get(self, request, format=None):
		request.user.auth_token.delete()
		return Response(status=status.HTTP_200_OK)

'''
GET Orders methods
'''
# Get Orders for a user
def getOrdersForUser(request, userId, format=None): 
	pass

# Get Order with number Id
def getOrderWithOrderNumber(request, orderNumber, format=None):
	pass