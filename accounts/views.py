from django.shortcuts import render, get_object_or_404
from rest_framework import generics, permissions, authentication, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, SignupSerializer, LoginSerializer, \
    RequestPasswordResetEmailSerializer, SetNewPasswordSerializer
from .models import CustomUser, Profile, BitsSchool
from drf_yasg.utils import swagger_auto_schema
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_bytes, smart_str, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .utils import Util
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .renderers import UsersRenderers, UserRegistrationRenderers, UserDetailRenderers

# # Create your views here.


class UserListAPI(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    renderer_classes = (UsersRenderers,)


class UserDetailsAPI(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    lookup_field = 'id'
    serializer_class = UserSerializer
    renderer_classes = (UserDetailRenderers,)


class SignupAPI(APIView):
    renderer_classes = (UserRegistrationRenderers,)
    first_name = openapi.Schema(type=openapi.TYPE_STRING)
    last_name = openapi.Schema(type=openapi.TYPE_STRING)
    email = openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_EMAIL)
    phone_number = openapi.Schema(type=openapi.TYPE_STRING)
    bits_school = openapi.Schema(type=openapi.TYPE_STRING)
    year_of_graduation = openapi.Schema(type=openapi.TYPE_STRING)
    country = openapi.Schema(type=openapi.TYPE_STRING)
    properties = {"first_name": first_name, "last_name": last_name, "email": email, "phone_number": phone_number,
                  "bits_school": bits_school, "year_of_graduation": year_of_graduation, "country": country}

    @swagger_auto_schema(request_body=openapi.Schema(type=openapi.TYPE_OBJECT,
                                                     required=['first_name', 'last_name', 'email', 'phone_number',
                                                               'bits_school', 'year_of_graduation', 'country'],
                                                     properties=properties))
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": "your account was successfully created. "
                                    "Account verification might take up to a week"},
                        status=status.HTTP_201_CREATED)


class LoginAPI(APIView):
    renderer_classes = (UserRegistrationRenderers,)

    @swagger_auto_schema(request_body=openapi.Schema(type=openapi.TYPE_OBJECT,
                                                     required=['email', 'password'],
                                                     properties={'email': openapi.Schema(type=openapi.TYPE_STRING,
                                                                                         format=openapi.FORMAT_EMAIL),
                                                                 'password': openapi.Schema(type=openapi.TYPE_STRING,
                                                                                            format=openapi.FORMAT_PASSWORD)
                                                                 }))
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RequestPasswordResetAPI(APIView):
    @swagger_auto_schema(request_body=openapi.Schema(type=openapi.TYPE_OBJECT,
                                                     required=['email'],
                                                     properties={'email': openapi.Schema(type=openapi.TYPE_STRING,
                                                                                         format=openapi.FORMAT_EMAIL)
                                                                }))
    def post(self, request):
        serializer = RequestPasswordResetEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = request.data.get('email', {})
        if CustomUser.objects.filter(email=email).exists():
            user = CustomUser.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(request=request).domain
            relative_link = reverse('password-reset-token-check', kwargs={'uidb64': uidb64, 'token': token})
            absurl = 'http://' + '127.0.0.1:8000' + relative_link
            email_body = "Hello, \n use the link below to reset your password \n" + absurl
            data = {
                'email_body': email_body,
                'to_email': user.email,
                'email_subject': 'Reset your password'
            }
            Util.send_email(data)
            return Response({"success": "Check your email for a reset password link"}, status=status.HTTP_200_OK)
        else:
            return Response({"success": "Check your email for a reset password link working"}, status=status.HTTP_200_OK)


class PasswordResetTokenCheck(APIView):

    def get(self, request, uidb64, token):
        try:
            user_id = smart_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(id=user_id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({"errors": "Token is not valid, request new one"},
                                status=status.HTTP_401_UNAUTHORIZED)
            return Response({"success": True, "message": "Credentials is valid", "uidb64": uidb64, "token": token},
                            status=status.HTTP_200_OK)
        except DjangoUnicodeDecodeError as identifier:
            return Response({"errors": "Token is temper with"}, status=status.HTTP_401_UNAUTHORIZED)


class SetNewPasswordAPI(APIView):
    renderer_classes = (UserRegistrationRenderers,)
    new_password = openapi.Schema(type=openapi.TYPE_STRING)
    confirm_password = openapi.Schema(type=openapi.TYPE_STRING)
    properties = {"new_password": new_password, "confirm_password": confirm_password}

    @swagger_auto_schema(request_body=openapi.Schema(type=openapi.TYPE_OBJECT,
                                                     required=['new_password', 'confirm_password'],
                                                     properties=properties))
    def patch(self, request):
        serializer = SetNewPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"success": True, "message": "Password reset successful"}, status=status.HTTP_201_CREATED)
