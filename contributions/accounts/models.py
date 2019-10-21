from django.db import models
from django.contrib.auth.models import AbstractBaseUser, Permission, BaseUserManager
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.

GENDER_TYPES = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class UserManager(BaseUserManager):

	def create_user(self, username, email, password=None):
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(username=username)
		user.set_password(password)
		user.email = email
		user.is_staff = True
		user.save()
		return user

	def create_superuser(self, username, password):
		user = self.create_user(username, email="", password=password)
		user.is_admin = True
		user.is_active = True
		user.save()
		return user

		


class User(AbstractBaseUser):
	username = models.CharField(max_length=50, unique=True)
	email = models.EmailField(max_length=255, unique=True)
	first_name = models.CharField(max_length=100, null=False)
	last_name = models.CharField(max_length=100, null=False)
	gender = models.CharField(choices=GENDER_TYPES, max_length=20)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	mobile = models.CharField(max_length=10, default='0', null=True)
	date_joined = models.DateTimeField( auto_now_add=True, auto_now=False)
	user_permissions = models.ManyToManyField(Permission, related_name='user_permissions', blank=True)

	objects = UserManager()

	USERNAME_FIELD = 'username'

	def __unicode__(self):
		return self.username

	def has_perm(self, perm, obj=None):
		if self.is_active and self.is_admin:
			return True
		else:
			try:
				user_perm = self.user_permissions.get(codename=perm)
			except ObjectDoesNotExist:
				user_perm = False
				return bool(user_perm)



    		









