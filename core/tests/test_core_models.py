from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from core.models import (Page, Home, WhoWeAre, Team, Testimonial, ContactEmail, ContactNumber,
                         Contact, SocialPlatform, FAQ,)
from accounts.models import CustomUser, BitsSchool
from faker import Faker


class TestViewSetup(APITestCase):
    pass
    # def create_bits_school(self):
    #     faker = Faker()
    #     bits_school = BitsSchool.objects.create(name=faker.name())
    #     return bits_school
    #
    # def create_tag(self):
    #     faker = Faker()
    #     tag = Tag.objects.create(name=faker.name())
    #     return tag
    #
    # def create_user(self):
    #     faker = Faker()
    #     bits_school = self.create_bits_school()
    #     user = CustomUser.objects.create_user(first_name=faker.name(), last_name=faker.name(), email=faker.email(),
    #                                           phone_number="081765443", password="password", bits_school=bits_school,
    #                                           year_of_graduation="2026", country="AF")
    #     return user
    #
    # def create_page(self):
    #     faker = Faker()
    #     name = faker.text()
    #     name = faker.name()
    #     page = Page.objects.create(name=name, paragraph='test event work', page_type=1, is_active=True)
    #     return page