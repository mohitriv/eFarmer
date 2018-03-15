from django.db import models

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.

# Users
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        """
        Creates and saves a User with the given email and all other fields.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            category=kwargs.get('category', None),
            name=kwargs.get('name', None),
            gender=kwargs.get('gender', None),
            identificationNumber=kwargs.get('identificationNumber', None),
            address=kwargs.get('address', None),
            phone=kwargs.get('phone', None),
            date_of_birth=kwargs.get('date_of_birth', None),
            is_active=kwargs.get('is_active', None),
            is_admin=kwargs.get('is_admin', None),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    category = models.CharField(max_length=10, null=False, blank=False)
    name = models.CharField(max_length=10, null=False, blank=False)
    gender = models.CharField(max_length=10, null=False, blank=False)
    identificationNumber = models.CharField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=500, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)

    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin


class Seller(User):
    objects = UserManager()

class Buyer(User):
    objects = UserManager()

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



