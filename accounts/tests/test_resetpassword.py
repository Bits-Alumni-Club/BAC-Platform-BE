# import json
# from django.core import mail
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase, APIClient
# from accounts.models import CustomUser, Profile
#
#
# class ResetPasswordTestCase(APITestCase):
#     client = APIClient()
#
#     def setUp(self):
#         self.valid_payload = {"first_name": "sylvester", "last_name": "okon", "email": "sylvesterokon@gmail.com",
#                               "phone_number": "1234545455", "password": "password1",
#                               "bits_school": "NGLG", "year_of_graduation": "2021", "country": "AF"}
#
#         self.send_mail_url = reverse('password-reset-email')
#
#     def test_reset_password_with_valid_details(self):
#         user = CustomUser.objects.all().last()
#         send_email = self.client.post(self.send_mail_url, data={"email": "jonas@gmail.com"}, format='json')
#         self.assertEqual(send_email.status_code, status.HTTP_200_OK)
#         # email_body = mail.outbox[0].body