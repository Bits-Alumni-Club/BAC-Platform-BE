# import json
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase, APIClient
# from accounts.models import CustomUser, Profile
#
#
# class LoginTest(APITestCase):
#     client = APIClient
#
#     def setUp(self):
#         self.valid_payload = {"first_name": "jonastest", "last_name": "jonas12", "email": "jonas012@gmail.com",
#                               "phone_number": "123455", "password": "password",
#                               "bits_school": "NGLG", "year_of_graduation": "2022", "country": "AF"}
#
#         self.valid_credentials = {"email": "jonas012@gmail.com",
#                                   "password": "password",
#                                   }
#
#         self.invalid_credentials = {"email": "jonas12@gmail.com",
#                                     "password": "password",
#                                     }
#
#         self.url = reverse('login')
#
#         self.create_account = self.client.post(self.url, data=self.valid_payload, format='json')
#
#     def test_login_with_valid_details(self):
#         create_account = self.client.post(self.url, data=self.valid_payload, format='json')
#         response = self.client.post(self.url, data=self.valid_credentials, format='json')
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
#
#     def test_login_with_invalid_details(self):
#         response = self.client.post(self.url, data=self.invalid_credentials, format='json')
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
#
#     def test_login_with_no_email(self):
#         response = self.client.post(self.url, data={"password": "password"}, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#
#     def test_login_with_no_password(self):
#         response = self.client.post(self.url, data={"email": "jonas12@gmail.com"}, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)