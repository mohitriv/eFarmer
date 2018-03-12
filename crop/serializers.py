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