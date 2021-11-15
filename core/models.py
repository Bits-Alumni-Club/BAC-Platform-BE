from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import CustomUser
# Create your models here.


class Page(models.Model):
    PAGE_TYPE_CHOICES = (
        (1, 'home'),
        (2, 'wwa'),
        (3, 'mission'),
        (4, 'vision'),
        (5, 'team'),
        (6, 'contact'),
        (7, 'testimony'),
        (8, 'faq'),
    )
    name = models.CharField(_('name'), max_length=100)
    paragraph = models.TextField(_('paragraph'))
    page_type = models.PositiveSmallIntegerField(_('Page Type'), choices=PAGE_TYPE_CHOICES,
                                                 default=1)
    is_active = models.BooleanField(_('is active'), default=False)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    update_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __str__(self):
        return self.page_type


class Home(models.Model):
    page = models.ForeignKey(to=Page, on_delete=models.CASCADE)
    heading = models.CharField(_('heading'), max_length=500)
    image = models.ImageField(_('image'), upload_to='media/core/')
    display_time = models.DateTimeField(_('display time'), auto_now=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    update_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __str__(self):
        return self.heading

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Home'
        verbose_name = 'Home'


class WhoWeAre(models.Model):
    page = models.ForeignKey(to=Page, on_delete=models.CASCADE)
    heading = models.CharField(_('heading'), max_length=500)
    image = models.ImageField(_('image'), upload_to='media/core/')
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    update_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __str__(self):
        return self.heading

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Who We Are'
        verbose_name = 'Who We Are'


class Testimonial(models.Model):
    page = models.ForeignKey(to=Page, on_delete=models.CASCADE)
    user = models.ForeignKey(to=CustomUser, related_name='testimonials', on_delete=models.CASCADE)
    testimony = models.CharField(_('testimony'), max_length=500)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    update_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __str__(self):
        return self.user

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Testimonies'
        verbose_name = 'testimony'


class Team(models.Model):
    page = models.ForeignKey(to=Page, on_delete=models.CASCADE)
    team = models.ManyToManyField(to=CustomUser, related_name='teams')
    heading = models.CharField(_('heading'), max_length=500)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    update_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __str__(self):
        return self.team


class ContactEmail(models.Model):
    email = models.EmailField(_('email'))
    is_active = models.BooleanField(_('is active'), default=False)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    update_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __str__(self):
        return self.email


class ContactNumber(models.Model):
    number = models.CharField(_('phone number'), max_length=14)
    is_active = models.BooleanField(_('is active'), default=False)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    update_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __str__(self):
        return self.number


class SocialPlatform(models.Model):
    name = models.CharField(_('name'), max_length=150)
    link = models.URLField(_('link'))
    is_active = models.BooleanField(_('is active'), default=False)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    update_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    page = models.ForeignKey(to=Page, on_delete=models.CASCADE)
    heading = models.CharField(_('heading'), max_length=500)
    phone_number = models.ManyToManyField(to=ContactNumber, related_name='contact_numbers')
    email = models.ManyToManyField(to=ContactEmail, related_name='contact_emails')
    platform = models.ManyToManyField(to=SocialPlatform,  related_name='social_links')
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    update_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __str__(self):
        return self.page


class FAQ(models.Model):
    page = models.ForeignKey(to=Page, on_delete=models.CASCADE)
    question = models.CharField(_('question'), max_length=200)
    answer = models.TextField(_('answer'))
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    update_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __str__(self):
        return self.page


