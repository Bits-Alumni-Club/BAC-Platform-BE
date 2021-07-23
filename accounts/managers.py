from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext as _
import datetime


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email must be set')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        # if password is None:
        #     password = CustomUser.objects.make_random_password(length=10, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889")

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email must be set')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        # if not password:
        #     password = make_random_password(length=14, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889")
        #     user.set_password(password)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def _create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError('Email must be set')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_verified', True)
        extra_fields.setdefault('year_of_graduation', datetime.date.today().year)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have a is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have a is_superuser=True.'))
        return self._create_user(email, password, **extra_fields)
