from django.db import models

# Create your models here.

# Users
class User(models.Model):
	username = models.CharField(max_length=100, null=False, blank=False)
	password = models.CharField(max_length=500, null= False, blank=False)
	category = models.CharField(max_length=10, null=False, blank=False) # SELLER or BUYER
	name = models.CharField(max_length=100, null=False, blank=False)
	age = models.IntegerField(null=False, blank=False)
	gender = models.CharField(max_length=10, null=False, blank=False)
	identificationNumber = models.CharField(max_length=100, null=False, blank=False) # e.g. Driving license
	address = models.CharField(max_length=500, null=False, blank=False)
	phone = models.CharField(max_length=20, null=False, blank=False)
	email = models.CharField(max_length=100, null=False, blank=False)

	def __str__(self):
		return self.username

class Seller(User):
	pass

class Buyer(User):
	pass

# Crops
class Crop(models.Model):
    category = models.CharField(max_length=100, null=False, blank=False) # WHEAT, RICE

    def __str__(self):
        return self.category

class CropDetail(models.Model):
	crop = models.OneToOneField(Crop, on_delete=models.CASCADE, primary_key=True)
	seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True)
	availableWeight = models.FloatField() # Available weight
	lat = models.FloatField()
	lon = models.FloatField()

	def __str__(self):
		return self.crop.category

# Orders
class Order(models.Model):
	seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True)
	buyer = models.ForeignKey(Buyer, on_delete=models.SET_NULL, null=True)
	cropDetail = models.ForeignKey(CropDetail, on_delete=models.SET_NULL, null=True)
	
	orderNumber = models.CharField(max_length=100)
	quantityPurchased = models.IntegerField()
	orderDate = models.DateTimeField()
	expectedDeliveryDate = models.DateTimeField(null=True)
	actualDeliveryDate = models.DateTimeField(null=True)

	def __str__(self):
		return self.orderNumber



