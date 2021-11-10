import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from accounts.models import CustomUser, Profile
from accounts.serializers import UserSerializer, LoginSerializer, SignupSerializer


class UserTest(APITestCase):
    client = APIClient

    def setUp(self):
        self.user1 = {"first_name": "jonas101", "last_name": "john", "email": "jonasjohn@gmail.com",
                      "phone_number": "081765443", "password": "password", "bits_school": "NGLG",
                      "year_of_graduation": "2026", "country": "AF"}

        self.user2 = {"first_name": "david", "last_name": "alex", "email": "davidalex@gmail.com",
                      "phone_number": "081765443", "password": "password", "bits_school": "NGLG",
                      "year_of_graduation": "2026", "country": "AF"}

        self.url = reverse('users')
        self.url_get = reverse('user_detail', kwargs={'id': 1})

    def test_all_users(self):
        user_jonas = self.client.post(reverse('signup'), data=self.user1, format='json')
        users = self.client.get(self.url, format='json')
        self.assertEqual(users.status_code, status.HTTP_200_OK)
        # self.assertEqual(CustomUser.objects.all().count(), 2)

    def test_get_valid_single_user(self):
        user_david = self.client.post(reverse('signup'), data=self.user2, format='json')
        user = CustomUser.objects.all().last()
        single_user = self.client.get(reverse('user_detail', kwargs={'id': user.id}), format='json')
        self.assertEqual(single_user.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_user(self):
        single_user = self.client.get(reverse('user_detail', kwargs={'id': 300}), format='json')
        self.assertEqual(single_user.status_code, status.HTTP_404_NOT_FOUND)
