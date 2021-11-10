import json
import datetime
from django.core import mail
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase
from django.core import serializers
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
        bits_school = self.create_bits_school()
        bits_school_id = BitsSchool.objects.last()
        faker = Faker()
        payload = {"first_name": faker.name(), "last_name": faker.name(), "email": faker.email(),
                   "phone_number": "081765443", "password": "password", "bits_school": bits_school_id.id,
                   "year_of_graduation": "2026", "country": "AF"}

        create_resp = self.client.post(reverse('signup'), data=payload, format='json')
        resp = self.client.get(reverse('users'))
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_get_user_details(self):
        faker = Faker()
        bits_school = self.create_bits_school()
        user = CustomUser.objects.create_user(first_name=faker.name(), last_name=faker.name(), email=faker.email(),
                                              phone_number="081765443", password="password", bits_school=bits_school,
                                              year_of_graduation="2026", country="AF")
        resp = self.client.get(reverse('user_detail', kwargs={"id": user.id}))
        self.assertEqual(resp.status_code, status.HTTP_200_OK)


class TestSignUpViews(TestViewSetup):
    def test_signup_with_invalid_data(self):
        bits_school = self.create_bits_school()
        # bs = serializers.serialize("json", bits_school)
        faker = Faker()
        payload = {"first_name": faker.name(), "last_name": faker.name(),
                   "phone_number": "081765443", "password": "password", "bits_school": 1,
                   "year_of_graduation": "2026", "country": "AF"}
        resp = self.client.post(reverse('signup'), data=payload, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_valid_data(self):
        bits_school = self.create_bits_school()
        # bs = serializers.serialize("json", bits_school)
        bits_school_id = BitsSchool.objects.last()
        faker = Faker()
        payload = {"first_name": faker.name(), "last_name": faker.name(), "email": faker.email(),
                   "phone_number": "081765443", "password": "password", "bits_school": bits_school_id.id,
                   "year_of_graduation": "2026", "country": "AF"}

        resp = self.client.post(reverse('signup'), data=payload, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)


class TestLogInViews(TestViewSetup):
    def test_login_with_invalid_data(self):
        bits_school = self.create_bits_school()
        faker = Faker()
        email = faker.email()
        password = "password"
        payload = {"first_name": faker.name(), "last_name": faker.name(), "email": email,
                   "phone_number": "081765443", "password": password, "bits_school": 1,
                   "year_of_graduation": "2026", "country": "AF"}

        resp = self.client.post(reverse('login'), data={"email": email, "password": "password1"}, format='json')
        self.assertEqual(resp.status_code, 401)

    def test_login_with_valid_and_unverified_account(self):
        bits_school = self.create_bits_school()
        faker = Faker()
        email = faker.email()
        password = "password"
        payload = {"first_name": faker.name(), "last_name": faker.name(), "email": email,
                   "phone_number": "081765443", "password": password, "bits_school": 1,
                   "year_of_graduation": "2026", "country": "AF"}

        resp = self.client.post(reverse('login'), data={"email": email, "password": password}, format='json')
        self.assertEqual(resp.status_code, 401)

    def test_login_with_valid_and_verified_account(self):
        faker = Faker()
        bits_school = BitsSchool.objects.create(name="NG1")
        email = faker.email()
        password = "password"
        payload = {"first_name": faker.name(), "last_name": faker.name(), "email": email,
                   "phone_number": "081765443", "password": password, "bits_school": bits_school.id,
                   "year_of_graduation": "2026", "country": "AF"}
        signup = self.client.post(reverse('signup'), data=payload, format='json')
        user = CustomUser.objects.get(email=email)
        user.is_verified = True
        user.is_active = True
        user.save()
        resp = self.client.post(reverse('login'), data={"email": email, "password": password}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)


class TestForgotPasswordViews(TestViewSetup):
    def test_forgot_password_with_unexisting_email(self):
        resp = self.client.post(reverse('password-reset-email'), data={"email": "dele12@gmail.com"}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(mail.outbox), 0)

    def test_forgot_password_with_existing_email(self):
        faker = Faker()
        bits_school = BitsSchool.objects.create(name="NG1")
        email = faker.email()
        password = "password"
        payload = {"first_name": faker.name(), "last_name": faker.name(), "email": email,
                   "phone_number": "081765443", "password": password, "bits_school": bits_school.id,
                   "year_of_graduation": "2026", "country": "AF"}
        signup = self.client.post(reverse('signup'), data=payload, format='json')
        user = CustomUser.objects.get(email=email)
        user.is_verified = True
        user.is_active = True
        user.save()
        resp = self.client.post(reverse('password-reset-email'), data={"email": email}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(mail.outbox), 1)


class TestResetPasswordViews(TestViewSetup):
    def test_password_reset_invalid_link(self):
        faker = Faker()
        bits_school = BitsSchool.objects.create(name="NG1")
        email = faker.email()
        password = "password"
        payload = {"first_name": faker.name(), "last_name": faker.name(), "email": email,
                   "phone_number": "081765443", "password": password, "bits_school": bits_school.id,
                   "year_of_graduation": "2026", "country": "AF"}
        signup = self.client.post(reverse('signup'), data=payload, format='json')
        user = CustomUser.objects.get(email=email)
        user.is_verified = True
        user.is_active = True
        user.save()
        resp = self.client.post(reverse('password-reset-email'), data={"email": email}, format='json')

        # Email format body
        # http://127.0.0.1:8000/password-reset-token-check/MQ/avuurh-afedc57da2210c8891c1f40432747bf5/

        # collect uidb64, token from email body
        email_body = mail.outbox[0].body.splitlines()
        link = [i for i in email_body if "/password-reset-token-check/" in i][0]
        # uidb64, token, empty = link.split("/")[-3:]
        # email_data = {"uidb64": uidb64, "token": token}

        resp = self.client.patch(reverse('password-reset'),
                                data={"new_password": "password", "confirm_password": "password", "uidb64": "MA",
                                      "token": "av1urh-afedc57da2210c8891c1f40432747byet"},
                                format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_reset_valid_link(self):
        faker = Faker()
        bits_school = BitsSchool.objects.create(name="NG1")
        email = faker.email()
        password = "password"
        payload = {"first_name": faker.name(), "last_name": faker.name(), "email": email,
                   "phone_number": "081765443", "password": password, "bits_school": bits_school.id,
                   "year_of_graduation": "2026", "country": "AF"}
        signup = self.client.post(reverse('signup'), data=payload, format='json')
        user = CustomUser.objects.get(email=email)
        user.is_verified = True
        user.is_active = True
        user.save()
        resp = self.client.post(reverse('password-reset-email'), data={"email": email}, format='json')

        # Email format body

        # http://127.0.0.1:8000/password-reset-token-check/MQ/avuurh-afedc57da2210c8891c1f40432747bf5/

        # collect uidb64, token from email body

        email_body = mail.outbox[0].body.splitlines()
        link = [i for i in email_body if "/password-reset-token-check/" in i][0]
        uidb64, token, empty = link.split("/")[-3:]
        email_data = {"uidb64": uidb64, "token": token}

        resp = self.client.patch(reverse('password-reset'), data={"new_password": password,
                                                                 "confirm_password": password,
                                                                 "uidb64": email_data['uidb64'],
                                                                 "token": email_data['token']},
                                format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_login_after_password_reset_success(self):
        faker = Faker()
        bits_school = BitsSchool.objects.create(name="NG1")
        email = faker.email()
        password = "password"
        payload = {"first_name": faker.name(), "last_name": faker.name(), "email": email,
                   "phone_number": "081765443", "password": password, "bits_school": bits_school.id,
                   "year_of_graduation": "2026", "country": "AF"}
        signup = self.client.post(reverse('signup'), data=payload, format='json')
        user = CustomUser.objects.get(email=email)
        user.is_verified = True
        user.is_active = True
        user.save()
        resp = self.client.post(reverse('password-reset-email'), data={"email": email}, format='json')

        # Email format body
        # http://127.0.0.1:8000/password-reset-token-check/MQ/avuurh-afedc57da2210c8891c1f40432747bf5/

        # collect uidb64, token from email body
        email_body = mail.outbox[0].body.splitlines()
        link = [i for i in email_body if "/password-reset-token-check/" in i][0]
        uidb64, token, empty = link.split("/")[-3:]
        email_data = {"uidb64": uidb64, "token": token}
        resp = self.client.patch(reverse('password-reset'), data={"new_password": password,
                                                                 "confirm_password": password,
                                                                 "uidb64": email_data['uidb64'],
                                                                 "token": email_data['token']},
                                format='json')
        # Login
        login_resp = self.client.post(reverse('login'), data={"email": email, "password": password}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_login_after_password_reset_fail(self):
        faker = Faker()
        bits_school = BitsSchool.objects.create(name="NG1")
        email = faker.email()
        password = "password"
        payload = {"first_name": faker.name(), "last_name": faker.name(), "email": email,
                   "phone_number": "081765443", "password": password, "bits_school": bits_school.id,
                   "year_of_graduation": "2026", "country": "AF"}
        signup = self.client.post(reverse('signup'), data=payload, format='json')
        user = CustomUser.objects.get(email=email)
        user.is_verified = True
        user.is_active = True
        user.save()
        resp = self.client.post(reverse('password-reset-email'), data={"email": email}, format='json')

        # Email format body
        # http://127.0.0.1:8000/password-reset-token-check/MQ/avuurh-afedc57da2210c8891c1f40432747bf5/

        # collect uidb64, token from email body
        email_body = mail.outbox[0].body.splitlines()
        link = [i for i in email_body if "/password-reset-token-check/" in i][0]
        uidb64, token, empty = link.split("/")[-3:]
        email_data = {"uidb64": uidb64, "token": token}
        resp = self.client.patch(reverse('password-reset'), data={"new_password": "newpassword",
                                                                  "confirm_password": "newpassword",
                                                                  "uidb64": "QU",
                                                                  "token": email_data['token']},
                                 format='json')
        # Login
        login_resp = self.client.post(reverse('login'), data={"email": email, "password": "newpassword"}, format='json')
        self.assertEqual(login_resp.status_code, status.HTTP_401_UNAUTHORIZED)
