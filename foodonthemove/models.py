from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
import datetime



class AccountManager(BaseUserManager):
    def create_user(self, **kwargs):
        username = kwargs.get('username')
        number = kwargs.get('phone_number')
        if not username:
            raise ValueError('Users must have a valid username or equivalent')

        if number:
            number = ''.join(c for c in number if c.isdigit())
        email = self.normalize_email(kwargs.get('email'))

        account = self.model(
            username=username,
            is_admin=False,
        )

        account.set_password(kwargs.get('password'))
        account.save()

        return account

    def create_superuser(self, **kwargs):
        account = self.create_user(**kwargs)

        account.is_admin = True
        account.save()

        return account

class Account(AbstractBaseUser):
    email = models.EmailField(unique=True, blank=True, null=True)
    username = models.CharField(max_length=40, unique=True)
    phone_number = models.CharField(max_length=40, blank=True)

    contact_text = models.BooleanField(default=False)
    contact_call = models.BooleanField(default=False)
    contact_email = models.BooleanField(default=False)

    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)

    is_admin = models.BooleanField(default=False)

    address = models.CharField(max_length=40, blank=True)
    zip_code = models.CharField(max_length=20, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_paying = models.BooleanField(default=False)
    payment_amount = models.FloatField(null=True)

    objects = AccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __unicode__(self):
        return self.username

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
      return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
      return self.is_admin