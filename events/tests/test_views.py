from django.urls import reverse
from rest_framework.test import APITestCase
from django.core import serializers
from .test_setup import TestSetup
import datetime
from events.models import Event, EventGallery, Tag
from accounts.models import CustomUser, BitsSchool
from faker import Faker


class TestViewSetup(APITestCase):
    def create_bits_school(self):
        faker = Faker()
        bits_school = BitsSchool.objects.create(name=faker.name())
        return bits_school

    def create_tag(self):
        faker = Faker()
        tag = Tag.objects.create(name=faker.name())
        return tag

    def create_user(self):
        faker = Faker()
        bits_school = self.create_bits_school()
        user = CustomUser.objects.create_user(first_name=faker.name(), last_name=faker.name(), email=faker.email(),
                                              phone_number="081765443", password="password", bits_school=bits_school,
                                              year_of_graduation="2026", country="AF")
        return user

    def create_event(self):
        tag = self.create_tag()
        bits_school = self.create_bits_school()
        user = self.create_user()
        faker = Faker()
        title_words = ['title 1', 'title 2', 'title 3', 'title 4', 'title 5', 'title 6', 'title 7']
        title = faker.words(1, title_words, True)
        event = Event.objects.create(title=title, slug='test-title', description='test event work',
                                         is_active=True, no_of_attendant=20, location='lekki',
                                         link='https://www.google.com', start_date='2021-09-06',
                                         end_date='2021-10-06', image='', create_by=user)
        event.attendant.add(user)
        event.contact.add(user)
        event.save()
        return event

    def create_gallery(self):
        gallery = self.create_event()
        gallery.is_gallery = True
        gallery.save()
        return gallery


class TestTagViews(TestViewSetup):
    def test_tags(self):
        tag = self.create_tag()
        res = self.client.get(reverse('tags'))
        self.assertEqual(res.status_code, 200)

    def test_tag_details(self):
        tag = self.create_tag()
        res = self.client.get(reverse('tag', kwargs={'id': tag.id}))
        self.assertEqual(res.status_code, 200)


class TestEventViews(TestViewSetup):
    def test_get_all_events(self):
        tag = self.create_tag()
        bits_school = self.create_bits_school()
        user = self.create_user()

        event = self.create_event()
        res = self.client.get(reverse("events"))
        self.assertEqual(res.status_code, 200)

    def test_get_event_details(self):
        tag = self.create_tag()
        bits_school = self.create_bits_school()

        user = self.create_user()
        event = self.create_event()

        res = self.client.get(reverse("event", kwargs={"event_id": event.event_id}))
        self.assertEqual(res.status_code, 200)


class TestGalleryViews(TestViewSetup):
    def test_get_all_galleries(self):
        tag = self.create_tag()
        bits_school = self.create_bits_school()
        user = self.create_user()
        event = self.create_gallery()
        res = self.client.get(reverse("galleries"))
        self.assertEqual(res.status_code, 200)

    def test_get_gallery_details(self):
        tag = self.create_tag()
        bits_school = self.create_bits_school()
        user = self.create_user()
        event = self.create_gallery()

        res = self.client.get(reverse("gallery", kwargs={"event_id": event.event_id}))
        self.assertEqual(res.status_code, 200)

