from django.urls import path
from . import views
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from .serializers import LoginSerializer
from rest_framework.urlpatterns import format_suffix_patterns

# decorated_login_view = \
#    swagger_auto_schema(
#       method='post',
#       responses={status.HTTP_200_OK: LoginSerializer,}
#    )(views.LoginAPI.as_view())

# app_name = 'accounts'
urlpatterns = [
    path('users/', views.UserListAPI.as_view(), name='users'),
    path('users/<int:id>/', views.UserDetailsAPI.as_view(), name='user_detail'),
    path('signup/', views.SignupAPI.as_view(), name='signup'),
    path('login/', views.LoginAPI.as_view(), name='login'),
    path('password-reset-email/', views.RequestPasswordResetAPI.as_view(), name='password-reset-email'),
    path('password-reset/', views.SetNewPasswordAPI.as_view(), name='password-reset'),
    path('password-reset-token-check/<uidb64>/<token>/', views.PasswordResetTokenCheck.as_view(),
         name='password-reset-token-check'),
    path('bits-schools/', views.BitsSchoolAPI.as_view(), name='bits-schools'),
]

urlpatterns = format_suffix_patterns(urlpatterns)