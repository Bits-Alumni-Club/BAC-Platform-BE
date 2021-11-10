from rest_framework.test import APITestCase
from django.urls import reverse
from accounts.models import CustomUser, BitsSchool


class TestSetup(APITestCase):
    def setUp(self):
        self.users_url = reverse('users')
        self.userDetails_url = reverse('user_detail', kwargs={'id': 1})
        self.signUp_url = reverse('signup')
        self.logIn_url = reverse('login')
        self.forgotPassword_url = reverse('password-reset-email')
        self.setNewPassword_url = reverse('password-reset')
        self.passwordTokenCheck_url = reverse('password-reset-token-check')
        self.signUp_data_valid = {
            'first_name': 'dele',
            'last_name': 'joseph',
            'email': 'delejoseph@gmail.com',
            'phone_number': '090464673',
            'year_of_graduation': '2016',
            'bits_school': 'NGLG',
            'password': 'password',
            'country': 'AF',
        }

        self.signUp_data_invalid = {
            'first_name': 'dele',
            'last_name': 'joseph',
            'phone_number': '090464673',
            'bits_school': 'NGLG',
            'password': 'password',
            'country': 'AF',
        }

        self.logIn_data_valid = {
            'email': 'delejoseph@gmail.com',
            'password': 'password',
        }

        self.logIn_data_invalid = {
            'email': 'delejoseph@gmail.com',
            'password': '',
        }

        return self.super().setUp()

    def tearDown(self):
        self.users_url = reverse('users')
        self.userDetails_url = reverse('user_detail')
        self.signUp_url = reverse('signup')
        self.logIn_url = reverse('login')
        self.forgotPassword_url = reverse('password-reset-email')
        self.setNewPassword_url = reverse('password-reset')
        self.passwordTokenCheck_url = reverse('password-reset-token-check')

        return self.super().tearDown()
