from rest_framework import serializers, status
from rest_framework.response import Response
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from .models import CustomUser, Profile, BitsSchool
from django_countries.serializers import CountryFieldMixin
from drf_yasg.utils import swagger_serializer_method
from django.urls import reverse
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_bytes, smart_str, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.db import IntegrityError


# Create your serializers here.
class BitsSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = BitsSchool
        fields = ['name']


class UserSerializer(CountryFieldMixin, serializers.ModelSerializer):
<<<<<<< HEAD
<<<<<<< HEAD
    bits_school = serializers.ReadOnlyField(source='bits_school.name')
=======
    bits_school = BitsSchoolSerializer(many=True, read_only=True)
>>>>>>> 19c398321d7f117e952547bae164345e224ce6ad
=======
    bits_school = BitsSchoolSerializer(many=True, read_only=True)
>>>>>>> 19c398321d7f117e952547bae164345e224ce6ad

    class Meta:
        model = CustomUser
        fields = ["id", "user_id", "user_type", "first_name", "last_name", "email", "BAC_id", "slug", "is_active",
                  "phone_number", "bits_school", "year_of_graduation", "country", "certificate", "created_at",
                  "update_at"]
        lookup_field = ['id']


class SignupSerializer(CountryFieldMixin, serializers.ModelSerializer):
    password = serializers.CharField(max_length=20, allow_null=True, required=False)

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "phone_number", "bits_school", "year_of_graduation",
                  "country", "password"]

    def create(self, validated_data):
        password = validated_data['password']
        instances = self.Meta.model(**validated_data)

    def create(self, validated_data):
        password = validated_data.get('password', '')
        instances = self.Meta.model(**validated_data)
        if password == '':
            password = CustomUser.objects.make_random_password(length=10,
                                                               allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889")

            instances.set_password(password)
        if password is not None:
            instances.set_password(password)
        instances.save()
        return instances


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(allow_blank=False, )
    password = serializers.CharField(max_length=15, min_length=5, allow_blank=False, write_only=True)
    tokens = serializers.CharField(min_length=5, max_length=555, read_only=True)

    # class Meta:
    #     model = CustomUser
    #     fields = ["email", "password", "tokens"]

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        # if email and password:
        user = auth.authenticate(email=email, password=password)

        if user is None:
            raise AuthenticationFailed('Invalid login credentials.')
        if user.is_verified is False:
            raise AuthenticationFailed('You account verification still in progress.')
        if user.is_active is False:
            raise AuthenticationFailed('You account have been suspended, kindly contact Administration.')
        return {
            'email': user.email,
            'tokens': user.token
        }
        return super().validate(attrs)


class RequestPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=555, min_length=5)

    class Meta:
        fields = ["email"]


class SetNewPasswordSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(min_length=5, max_length=60, write_only=True)
    confirm_password = serializers.CharField(min_length=5, max_length=60, write_only=True)
    token = serializers.CharField(min_length=5, write_only=True)
    uidb64 = serializers.CharField(min_length=1, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['new_password', 'confirm_password', 'token', 'uidb64']

    def validate(self, data):
        new_password = data["new_password"]
        confirm_password = data["confirm_password"]
        token = data["token"]
        uidb64 = data["uidb64"]
        if new_password != confirm_password:
            raise serializers.ValidationError("Both password must match")
        try:
            user_id = force_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(id=user_id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise serializers.ValidationError("The reset link is invalid")
            # import pdb
            # pdb.set_trace()
            user.set_password(new_password)
            user.save()
            return user
        except Exception as e:
            raise serializers.ValidationError("The reset link is temper with")
        return super().validate(data)
