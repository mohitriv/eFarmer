from rest_framework import serializers

from .models import Crop, CropDetail, Buyer, Seller, User, Order


class CropSerializer(serializers.ModelSerializer):

	class Meta:
		model = Crop
		#fields = ('category')
		fields = '__all__'
		
class UserLimitedSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True, required=True)
	class Meta:
		model = User
		fields = ('id', 'email', 'category', 'name', 'gender', 'identificationNumber', 'address',
		'phone', 'date_of_birth', 'is_active', 'is_admin')
		read_only_fields = ('date_created', 'date_modified')

class CropDetailSerializer(serializers.ModelSerializer):
	myfield = UserLimitedSerializer() 
	class Meta:
		model = CropDetail
		fields = ('myfield', )
		depth = 1

class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True, required=True)
	is_active = serializers.BooleanField(required=False)
	is_admin = serializers.BooleanField(required=False)
	class Meta:
		model = User
		fields = ('id', 'email', 'category', 'name', 'gender', 'identificationNumber', 'address',
		'phone', 'date_of_birth', 'is_active', 'is_admin', 'password')
		read_only_fields = ('date_created', 'date_modified')

	def create(self, validated_data):
		return User.objects.create_user(**validated_data)

class SellerSerializer(UserSerializer):
	class Meta(UserSerializer.Meta):
		model = Seller
		fields = UserSerializer.Meta.fields

	def create(self, validated_data):
		return Seller.objects.create_user(**validated_data)

class BuyerSerializer(UserSerializer):
	class Meta(UserSerializer.Meta):
		model = Buyer
		fields = UserSerializer.Meta.fields

	def create(self, validated_data):
		return Buyer.objects.create_user(**validated_data)
			
		