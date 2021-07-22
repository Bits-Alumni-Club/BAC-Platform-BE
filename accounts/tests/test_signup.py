import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from accounts.models import CustomUser, Profile


class SignupTest(APITestCase):
    client = APIClient

    def setUp(self):
        self.valid_payload = {"first_name": "jonastest", "last_name": "jonas12", "email": "jonas012@gmail.com",
                              "phone_number": "123455", "password": "password",
                              "bits_school": "NGLG", "year_of_graduation": "2022", "country": "AF"}

        self.payload_no_first_name = {"last_name": "jonas12",
                                      "email": "jonas012@gmail.com",
                                      "phone_number": "123455", "password": "password",
                                      "bits_school": "NGLG", "year_of_graduation": "2022", "country": "AF"}

        self.payload_no_last_name = {"first_name": "jonastest", "email": "jonas012@gmail.com",
                                     "phone_number": "123455", "password": "password",
                                     "bits_school": "NGLG", "year_of_graduation": "2022", "country": "AF"}

        self.payload_no_email = {"first_name": "jonastest", "last_name": "jonas12",
                                 "phone_number": "123455", "password": "password",
                                 "bits_school": "NGLG", "year_of_graduation": "2022", "country": "AF"}

        self.payload_no_number = {"first_name": "jonastest", "last_name": "jonas12", "email": "jonas012@gmail.com",
                                  "password": "password",
                                  "bits_school": "NGLG", "year_of_graduation": "2022", "country": "AF"}

        self.payload_no_bits_school = {"first_name": "jonastest", "last_name": "jonas12", "email": "jonas012@gmail.com",
                                       "phone_number": "123455", "password": "password",
                                       "year_of_graduation": "2022", "country": "AF"}

        self.payload_no_year_of_graduation = {"first_name": "jonastest", "last_name": "jonas12",
                                              "email": "jonas012@gmail.com",
                                              "phone_number": "123455", "password": "password",
                                              "bits_school": "NGLG", "country": "AF"}

        self.payload_no_country = {"first_name": "jonastest", "last_name": "jonas12", "email": "jonas012@gmail.com",
                                   "phone_number": "123455", "password": "password",
                                   "bits_school": "NGLG", "year_of_graduation": "2022"}

        self.url = reverse('signup')

    def test_signup_with_valid_details(self):
        response = self.client.post(self.url, data=self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().email, 'jonas012@gmail.com')

    def test_signup_with_no_first_name(self):
        response = self.client.post(self.url, data=self.payload_no_first_name, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_with_no_last_name(self):
        response = self.client.post(self.url, data=self.payload_no_last_name, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_with_no_number(self):
        response = self.client.post(self.url, data=self.payload_no_number, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_with_no_email(self):
        response = self.client.post(self.url, data=self.payload_no_email, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_with_no_bits_school(self):
        response = self.client.post(self.url, data=self.payload_no_bits_school, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_with_no_year_of_graduation(self):
        response = self.client.post(self.url, data=self.payload_no_year_of_graduation, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_with_no_country(self):
        response = self.client.post(self.url, data=self.payload_no_country, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_with_exsting_email(self):
        response1 = self.client.post(self.url, data=self.valid_payload, format='json')
        response2 = self.client.post(self.url, data=self.valid_payload, format='json')

        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)
