from django.contrib import admin
from core.models import (Page, Home, WhoWeAre, Team, Testimonial, ContactEmail, ContactNumber,
                         Contact, SocialPlatform, FAQ,)

#
# class TeamInline(admin.TabularInline):
#     model = Team
#
#
# class PageAdmin(admin.ModelAdmin):
#     inlines = (TeamInline,)


class HomeInline(admin.TabularInline):
    model = Home
    extra = 1


class WhoWeAreInline(admin.TabularInline):
    model = WhoWeAre
    extra = 1


class TeamInline(admin.TabularInline):
    model = Team
    extra = 1


class TestimonialInline(admin.TabularInline):
    model = Testimonial
    extra = 1


class FAQInline(admin.TabularInline):
    model = FAQ
    extra = 1


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1


class PageAdmin(admin.ModelAdmin):
    inlines = (HomeInline, WhoWeAreInline, TeamInline, TestimonialInline, FAQInline, ContactInline)


admin.site.register(Page, PageAdmin)
admin.site.register(ContactEmail)
admin.site.register(ContactNumber)
admin.site.register(SocialPlatform)
