# import json
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase
from django.core import serializers
import datetime
from accounts.models import CustomUser, BitsSchool, Profile
from faker import Faker


class TestViewSetup(APITestCase):
    def create_bits_school(self):
        faker = Faker()
        bits_school = BitsSchool.objects.create(name=faker.name())
        return bits_school

    def create_user(self):
        faker = Faker()
        bits_school = self.create_bits_school()
        user = CustomUser.objects.create_user(first_name=faker.name(), last_name=faker.name(), email=faker.email(),
                                              phone_number="081765443", password="password", bits_school=bits_school,
                                              year_of_graduation="2026", country="AF")
        return user


class TestUserViews(TestViewSetup):
    def test_get_all_users(self):
        pass

    def test_get_user_details(self):
        pass


class TestSignUpViews(TestViewSetup):
    def test_signup_with_invalid_data(self):
        pass

    def test_signup_valid_data(self):
        pass

    def test_signup_with_unverified_account(self):
        pass

    def test_signup_with_verified_account(self):
        pass


class TestLogInViews(TestViewSetup):
    def test_login_with_invalid_data(self):
        pass

    def test_login_with_valid_and_unverified_account(self):
        pass

    def test_login_with_valid_and_verified_account(self):
        pass


class TestForgotPasswordViews(TestViewSetup):
    def test_forgot_password_with_unexisting_email(self):
        pass

    def test_forgot_password_with_existing_email(self):
        pass


class TestResetPasswordViews(TestViewSetup):
    def test_password_reset_invalid_link(self):
        pass

    def test_password_reset_valid_link(self):
        pass

    def test_login_after_password_reset_success(self):
        pass

    def test_login_after_password_reset_fail(self):
        pass



#
#
# class TestUsers(TestSetup):
#     def test_get_users(self):
#         res=self.client.get(self.users_url)
#         self.assertEqual(res.status_code, status.HTTP_200_OK)
#
#     def test_get_user(self):
#         res=self.client.get(self.userDetails_url)
#         self.assertEqual(res.status_code, status.HTTP_200_OK)
#
#
# class TestSignUp(TestSetup):
#     def test_signup_with_no_filling_required_field(self):
#         res=self.client.post(self.signUp_url, data=self.user_data_invalid, format='json')
#         self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
#
#     def test_signup_with_valid_details(self):
#         res=self.client.post(self.signUp_url, data=self.user_data_valid, format='json')
#         self.assertEqual(res.status_code, status.HTTP_200_OK)
#
#
# class TestLogin(TestSetup):
#     def test_login_with_no_required_field(self):
#         signup = self.client.post(self.signUp_url, data=self.signUp_data_invalid, format='json')
#         res=self.client.post(self.logIn_url, data=self.logIn_data_invalid, format='json')
#         self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
#
#     def test_login_with_account_not_verified(self):
#         signup = self.client.post(self.signUp_url, data=self.user_data_valid)
#         verify = CustomUser.objects.filter(email=signup.data['email'])
#         cred = {"email": signup.data['email'], "password": signup.data['password']}
#         res=self.client.post(self.logIn_url, data=cred, format='json')
#         self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
#
#     def test_login_with_verified_account(self):
#         signup = self.client.post(self.signUp_url, data=self.user_data_valid)
#         verify = CustomUser.objects.filter(email=signup.data['email'])
#         verify.is_verified = True
#         verify.is_active = True
#         verify.save()
#         cred = {"email": signup.data['email'], "password": signup.data['password']}
#         res=self.client.post(self.logIn_url, data=cred, format='json')
#         self.assertEqual(res.status_code, status.HTTP_200_OK)
#
#     def test_login_with_no_required_field(self):
#         signup = self.client.post(self.signUp_url, data=self.user_data_invalid)
#         cred = {"email": signup.data['email'], "password": signup.data['password']}
#         res=self.client.post(self.logIn_url, data=cred, format='json')
#         self.assertEqual(res.status_code, status.HTTP_200_OK)
#
#
# class TestPasswordResetEmail(TestSetup):
#     def test_forgot_password_with_no_email(self):
#         res=self.client.post(self.forgotPassword_url)
#         self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
#
#     def test_forgot_password_with_no_email(self):
#         signup = self.client.post(self.signUp_url, data=self.user_data_invalid)
#         cred = {"email": signup.data['email']}
#         res=self.client.post(self.forgotPassword_url, data=cred, format='json')
#         self.assertEqual(res.status_code, status.HTTP_200_OK)
#
#
# class TestResetPassword(TestSetup):
#     def test_reset_password_with_no_password(self):
#         signup = self.client.post(self.signUp_url, data=self.user_data_invalid)
#         cred = {"email": signup.data['email']}
#         forgot_password=self.client.post(self.forgotPassword_url, data=cred, format='json')
#
#     #     res = self.client.post(self.setNewPassword_url)
#     #     self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
#     #
#     # def test_forgot_password_with_no_email(self):
#     #     signup = self.client.post(self.signUp_url, data=self.user_data_invalid)
#     #     cred = {"email": signup.data['email']}
#     #     res = self.client.post(self.forgotPassword_url, data=cred, format='json')
#     #     self.assertEqual(res.status_code, status.HTTP_200_OK)
#
# # class UserTest(APITestCase):
# #     def setUp(self):
# #         self.user1 = CustomUser.objects.create(first_name="jonas", last_name="john", email="jonasjohn@gmail.com",
# #                                                phone_number="081765443", password="password", bits_school="NGLG",
# #                                                year_of_graduation="2022", country="AF")
# #
# #         self.user2 = CustomUser.objects.create(first_name="david", last_name="alex", email="davidalex@gmail.com",
# #                                                phone_number="0908366454", password="password", bits_school="NGLG",
# #                                                year_of_graduation="2022", country="AF")
# #
# #         self.login_url = reverse('login')
#
#