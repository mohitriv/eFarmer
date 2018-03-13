from rest_framework import serializers

from .models import Crop, CropDetail, Buyer, Seller, User, Order


class CropSerializer(serializers.ModelSerializer):

	class Meta:
		model = Crop
		#fields = ('category')
		fields = '__all__'
		

class CropDetailSerializer(serializers.ModelSerializer):

	class Meta:
		model = CropDetail
		fields = '__all__'
		depth = 1


class UserSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = User
		exclude = ('password', )

class SellerSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Seller
		exclude = ('password', )

class BuyerSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Buyer
		exclude = ('password', )
			
		