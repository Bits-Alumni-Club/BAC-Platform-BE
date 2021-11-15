from rest_framework import serializers
from accounts.models import CustomUser
from core.models import (Page, Home, WhoWeAre, Team, Testimonial, ContactEmail, ContactNumber,
                         Contact, SocialPlatform, FAQ,)


class PageSerializer(serializers.ModelSerializer):
    pass


class HomeSerializer(serializers.ModelSerializer):
    pass


class WhoWeAreSerializer(serializers.ModelSerializer):
    pass


class TeamSerializer(serializers.ModelSerializer):
    pass


class TestimonySerializer(serializers.ModelSerializer):
    pass


class ContactSerializer(serializers.ModelSerializer):
    pass


class FAQSerializer(serializers.ModelSerializer):
    pass
