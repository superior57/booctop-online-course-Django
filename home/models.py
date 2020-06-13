# from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import Group, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class UserManager(BaseUserManager):

    def create_user(self, email,
                    password=None,
                    is_superuser=False,
                    is_staff=False,
                    is_active=True):
        user = User(email=email,
                    is_superuser=is_superuser,
                    is_staff=is_staff,
                    is_active=is_active)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        return self.create_user(email,
                                password=password,
                                is_superuser=True,
                                is_staff=True,
                                is_active=True)

class User(AbstractBaseUser):
    
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(_("staf status"), default=False)
    is_active = models.BooleanField(_("active"), default=True)
    is_superuser = models.BooleanField(_("superuser status"), default=False)
    is_confirmed = models.BooleanField(default=False, verbose_name ="Is confirmed")
    date_joined = models.DateTimeField(_("date joined"), default= timezone.now())
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    image = models.TextField(null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING)
    USERNAME_FIELD ="email"

    objects = UserManager()
    
    class Meta():
        verbose_name = _("User")
        verbose_name_plural = _("Users")
    
    def has_perm(self, perm, obj=None): 
        return self.is_superuser

    def has_module_perms(self, app_label): 
        return self.is_superuser




class user_activation(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    code = models.CharField(max_length=70)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)




