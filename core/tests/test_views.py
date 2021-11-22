import django
django.setup()
from django.urls import reverse
from rest_framework import status
from core.models import (Page, Home, WhoWeAre, Team, Testimonial, ContactEmail, ContactNumber,
                    Contact, SocialPlatform, FAQ,)
from accounts.models import CustomUser, BitsSchool
from rest_framework.test import APITestCase
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


class TestPageView(TestViewSetup):
    def test_get_all_pages(self):
        res = self.client.get(reverse('page'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)


class TestHomeView(TestViewSetup):
    def test_get_home(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)


class TestTeamView(TestViewSetup):
    def test_get_team(self):
        res = self.client.get(reverse('teams'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)


class TestWhoWeAreView(TestViewSetup):
    def test_get_who_we_are(self):
        res = self.client.get(reverse('wwa'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)


class TestTestimonialView(TestViewSetup):
    def test_get_testimonial(self):
        res = self.client.get(reverse('testimonials'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)


class TestTestimonialView(TestViewSetup):
    def test_get_faq(self):
        res = self.client.get(reverse('faq'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)


class TestContactView(TestViewSetup):
    def test_get_contact(self):
        res = self.client.get(reverse('contacts'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)