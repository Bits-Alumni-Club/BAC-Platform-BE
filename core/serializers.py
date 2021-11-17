from rest_framework import serializers
from accounts.models import CustomUser
from core.models import (Page, Home, WhoWeAre, Team, Testimonial, ContactEmail, ContactNumber,
                         Contact, SocialPlatform, FAQ,)
from accounts.serializers import UserSerializer


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('name', 'paragraph', 'page_type', 'is_active', 'created_at', 'updated_at',)


class HomeSerializer(serializers.ModelSerializer):
    page = PageSerializer(read_only=True)

    class Meta:
        model = Home
        fields = ('page', 'heading', 'image', 'display_time', 'created_at', 'updated_at',)


class WhoWeAreSerializer(serializers.ModelSerializer):
    page = PageSerializer(read_only=True)

    class Meta:
        model = WhoWeAre
        fields = ('page', 'heading', 'image', 'created_at', 'updated_at',)


# class CustomUserSerializer(serializers.ModelSerializer):
#     model = CustomUser
#     fields = ('id', 'user_id', 'user_type', 'first_name', 'last_name', 'email', 'BAC_id', 'slug', 'is_active',
#               'is_verified', 'phone_number', 'bits_school', 'year_of_graduation', 'country', 'certificate', 'created_at',
#               'update_at',)


class TeamSerializer(serializers.ModelSerializer):
    page = PageSerializer(read_only=True)
    team = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ('page', 'heading', 'team', 'created_at', 'updated_at',)


class TestimonySerializer(serializers.ModelSerializer):
    page = PageSerializer(read_only=True)
    team = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Testimonial
        fields = ('page', 'team', 'testimony', 'created_at', 'updated_at',)


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactEmail
        fields = ('email', 'is_active', 'created_at', 'updated_at',)


class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactNumber
        fields = ('number', 'is_active', 'created_at', 'updated_at',)


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialPlatform
        fields = ('name', 'link', 'is_active', 'created_at', 'updated_at',)


class ContactSerializer(serializers.ModelSerializer):
    page = PageSerializer(read_only=True)
    email = EmailSerializer(many=True, read_only=True)
    phone_number = NumberSerializer(many=True, read_only=True)

    class Meta:
        model = Contact
        fields = ('page', 'platform', 'heading', 'phone_number', 'email', 'created_at', 'updated_at',)


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ('page', 'question', 'answer', 'created_at', 'updated_at',)
