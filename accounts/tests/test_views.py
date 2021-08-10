import json
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from accounts.models import CustomUser, Profile


class UserTest(APITestCase):
    def setUp(self):
        self.user1 = CustomUser.objects.create(first_name="jonas", last_name="john", email="jonasjohn@gmail.com",
                                               phone_number="081765443", password="password", bits_school="NGLG",
                                               year_of_graduation="2022", country="AF")

        self.user2 = CustomUser.objects.create(first_name="david", last_name="alex", email="davidalex@gmail.com",
                                               phone_number="0908366454", password="password", bits_school="NGLG",
                                               year_of_graduation="2022", country="AF")

        self.login_url = reverse('login')


