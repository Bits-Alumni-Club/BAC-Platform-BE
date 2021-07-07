import uuid
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

# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
    EKO_BITS = 'NGLG'
    EDO_BITS = 'NGBN'
    BITS_SCHOOL_CHOICES = [
        (EKO_BITS, 'Eko Bits'),
        (EDO_BITS, 'Edo Bits'),
    ]
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(_('first name'), max_length=50)
    last_name = models.CharField(_('last name'), max_length=50)
    slug = models.SlugField(_('slug'), max_length=255, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    BAC_id = models.CharField(max_length=255)
    is_active = models.BooleanField(_('is active'), default=False)
    phone_number = models.CharField(_('phone number'), max_length=14)
    bits_school = models.CharField(_('bits school'), max_length=20, choices=BITS_SCHOOL_CHOICES)
    year_of_graduation = models.DateField(_('year of graduation'), blank=False)
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

    def auto_id(self):
        return 'BAC'+self.year_of_graduation+self.id

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.first_name + '-' + self.last_name)
        if not self.BAC_ID:
            self.BAC_ID = self.auto_id()
        return super().save(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(to=CustomUser, on_delete=models.CASCADE)
    profile_image = models.ImageField(_('profile photo'))
    bio = models.CharField(_('Bio'), max_length=255, null=True, blank=True)
    birthdate = models.DateField(_('date of birth'), null=True, blank=True)
    website_link = models.URLField(_('website link'))
    portfolio_link = models.URLField(_('portfolio link'))
    facebook_profile = models.URLField(_('facebook profile'))
    twitter_profile = models.URLField(_('twitter profile'))
    linkedin_profile = models.URLField(_('linkedIn profile'))
    skill_sets = models.CharField(_('skill sets'), max_length=255, null=True, blank=True)


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    # if created:
    #     Artist.objects.create(user=instance)
    try:
        instance.artist.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Event(models.Model):
    pass