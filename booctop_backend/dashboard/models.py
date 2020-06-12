from django.db import models
from django.contrib.auth.models import User
from .choices import USER_TYPE
from ckeditor.fields import RichTextField

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_pic = models.ImageField(upload_to='user_profile', null=True, blank=True)
	phone_number = models.CharField(max_length=16)
	user_type = models.CharField(max_length=10, choices=USER_TYPE)
	activation_code = models.UUIDField()

	def __str__(self):
		return self.user.username + ' profile'

class TermsAndConditions(models.Model):
	title = models.CharField(max_length=255)
	description = RichTextField()
	version = models.CharField(max_length=12)