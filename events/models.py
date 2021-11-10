from django.db import models
from accounts.models import CustomUser, BitsSchool
import uuid
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

# Create your models here.


class Event(models.Model):
    event_id = models.UUIDField(_('event id'), unique=True, default=uuid.uuid4, editable=False)
    title = models.CharField(_('title'), max_length=150)
    slug = models.SlugField(_('slug'), max_length=255, unique=True)
    description = models.TextField(_('description'))
    is_active = models.BooleanField(_('is_active'), default=False)
    no_of_attendant = models.PositiveIntegerField(_('number of attendant'))
    location = models.CharField(_('location'), max_length=255)
    link = models.CharField(_('link'), max_length=255, blank=True)
    start_date = models.DateTimeField(_('start date'))
    end_date = models.DateTimeField(_('end date'))
    image = models.ImageField(_('image'), upload_to='media/events/')
    is_gallery = models.BooleanField(_('is gallery'), default=False)
    create_by = models.ForeignKey(to=CustomUser, on_delete=models.SET_DEFAULT, default="deleted")
    tag = models.ManyToManyField(to='Tag')
    attendant = models.ManyToManyField(to=CustomUser, related_name='attendants')
    contact = models.ManyToManyField(to=CustomUser, related_name='contacts')
    bit_school = models.ManyToManyField(to=BitsSchool,)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated_at'), auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    

class Tag(models.Model):
    name = models.CharField(_('name'),  max_length=150)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated_at'), auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class EventGallery(models.Model):
    event = models.ForeignKey(to=Event, related_name='galleries', on_delete=models.CASCADE)
    images = models.ImageField(_('images'), upload_to='media/galleries/')
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated_at'), auto_now=True)

    def __str__(self):
        return self.event.title

    class Meta:
        verbose_name_plural = 'Galleries'
        verbose_name = 'gallery'





