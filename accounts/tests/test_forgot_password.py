# import json
# from django.urls import reverse
# from rest_framework.test import APITestCase, APIClient
# from rest_framework import status
# from accounts.models import CustomUser, Profile
#
#
# class RestPasswordEmail(APITestCase):
#     client = APIClient
#
#     def setUp(self):
#         self.user1 = {"first_name": "jonas101", "last_name": "john", "email": "jonasjohn@gmail.com",
#                       "phone_number": "081765443", "password": "password", "bits_school": "NGLG",
#                       "year_of_graduation": "2026", "country": "AF"}
#
#         self.user2 = {"first_name": "david", "last_name": "alex", "email": "davidalex",
#                       "phone_number": "081765443", "password": "password", "bits_school": "NGLG",
#                       "year_of_graduation": "2026", "country": "AF"}
#
#         self.user3 = {"first_name": "ken", "last_name": "obi", "email": "obi12@gmail.com",
#                       "phone_number": "08188765443", "password": "password", "bits_school": "NGLG",
#                       "year_of_graduation": "2022", "country": "AF"}
#
#         self.payload1 = {"email": "jonasjohn@gmail.com"}
#         self.payload2 = {"email": "davidalex"}
#         self.payload3 = {"email": "noneemail@gmail.com"}
#
#         self.signup_url = reverse('signup')
#         self.forgot_password_url = reverse('password-reset-email')
#
#     def test_with_valid_email(self):
#         user = self.client.post(reverse('signup'), data=self.user1, format='json')
#         email_response = self.client.post(reverse('password-reset-email'), data=self.payload1, format='json')
#         self.assertEqual(email_response.status_code, status.HTTP_200_OK)
#
#     def test_with_invalid_email(self):
#         email_response = self.client.post(reverse('password-reset-email'), data=self.payload2, format='json')
#         self.assertEqual(email_response.status_code, status.HTTP_400_BAD_REQUEST)
#
#     def test_with_unregister_email(self):
#         user = self.client.post(reverse('signup'), data=self.user1, format='json')
#         email_response = self.client.post(reverse('password-reset-email'), data=self.payload3, format='json')
#         self.assertEqual(email_response.status_code, status.HTTP_200_OK)
#
