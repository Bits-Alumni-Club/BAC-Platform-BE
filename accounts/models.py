import uuid
import jwt
from django.db import models
from django_countries.fields import CountryField
# from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import post_save
from .managers import CustomUserManager
from rest_framework_simplejwt.tokens import RefreshToken


# Create your models here.

class BitsSchool(models.Model):
    name = models.CharField(_('bits school name'), max_length=200)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    update_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Bits Schools'
        verbose_name = 'Bits School'


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True, unique=True, editable=False)
    user_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    slug = models.SlugField(_('slug'), max_length=255, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    BAC_id = models.CharField(_('BAC id'), max_length=255)
    is_active = models.BooleanField(_('is active'), default=False)
    is_verified = models.BooleanField(_('is verified'), default=False)
    is_staff = models.BooleanField(_('is staff'), default=False)
    phone_number = models.CharField(_('phone number'), max_length=14)
    year_of_graduation = models.CharField(_('year of graduation'), max_length=20, blank=False)
    bits_school = models.ForeignKey(BitsSchool, on_delete=models.SET_NULL, null=True)
    country = CountryField(_('country'))
    certificate = models.FileField(_('certificate'))
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    update_at = models.DateTimeField(_('updated at'), auto_now=True)

    USER_TYPE_CHOICES = (
        (1, 'alumni'),
        (2, 'excos'),
        (3, 'admin'),
    )
    user_type = models.PositiveSmallIntegerField(_('User Type'), choices=USER_TYPE_CHOICES,
                                                 default=1)

    def __str__(self):
        return self.first_name+'-'+self.last_name

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Users'
        verbose_name = 'User'

    def auto_generated_id(self):
        if self.id:
            if len(str(self.id)) == 1:
                return 'BAC'+str(self.year_of_graduation)+'000'+str(self.id)
            if len(str(self.id)) == 2:
                return 'BAC'+str(self.year_of_graduation)+'00'+str(self.id)
            if len(str(self.id)) == 3:
                return 'BAC'+str(self.year_of_graduation)+'0'+str(self.id)
            if len(str(self.id)) == 4:
                return 'BAC'+str(self.year_of_graduation)+str(self.id)
            return 'BAC' + str(self.year_of_graduation) + str(self.id)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.first_name + '-' + self.last_name)
        if self.id is None:
            super().save(*args, **kwargs)
            if not self.BAC_id:
                self.BAC_id = self.auto_generated_id()
        super().save(*args, **kwargs)

    def token(self):
        refresh = RefreshToken.for_user(self)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }


class Profile(models.Model):
    user = models.OneToOneField(to=CustomUser, on_delete=models.CASCADE)
    profile_image = models.ImageField(_('profile photo'))
    bio = models.CharField(_('Bio'), max_length=255, null=True, blank=True)
    dob = models.DateField(_('date of birth'), null=True, blank=True)
    website_link = models.URLField(_('website link'))
    portfolio_link = models.URLField(_('portfolio link'))
    facebook_profile = models.URLField(_('facebook profile'))
    twitter_profile = models.URLField(_('twitter profile'))
    linkedin_profile = models.URLField(_('linkedIn profile'))
    skill_sets = models.CharField(_('skill sets'), max_length=255, null=True, blank=True)
    extra_field = models.CharField(_('test'), max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Profile'


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    # if created:
    #     Artist.objects.create(user=instance)
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    # if created:
    #     Artist.objects.create(user=instance)
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)

