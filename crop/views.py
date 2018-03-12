from django.http import HttpResponse, JsonResponse

from django.shortcuts import get_object_or_404

from .models import Crop, CropDetail, User, Seller, Buyer, Order

from .serializers import CropSerializer, CropDetailSerializer

# Create your views here.

'''
GET Crops methods
'''
# Get all Crops
def getCrops(request):
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

# Get Crop with id
def getCropWithId(request, cropId):
	crop = get_object_or_404(Crop, pk=cropId)
	cropSerializer = CropSerializer(crop)
	return JsonResponse(cropSerializer.data)

# Get Crop detail with id
def getCropDetail(request, cropId):
	cropDetail = get_object_or_404(CropDetail, crop__id=cropId)
	cropDetailSerializer = CropDetailSerializer(cropDetail)
	return JsonResponse(cropDetailSerializer.data)

'''
GET Users methods
'''
# Get all Users
def getUsers(request):
	pass

# Get User with id
def getUserWithId(request, userId):
	pass

'''
GET Orders methods
'''
# Get Orders for a user
def getOrdersForUser(request, userId): 
	pass

# Get Order with number Id
def getOrderWithOrderNumber(request, orderNumber):
	pass