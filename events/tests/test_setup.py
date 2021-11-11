# from django.utils import timezone
# from django.urls import reverse
# from accounts.models import CustomUser, BitsSchool
# from events.models import Tag, Event
# from rest_framework.test import APITestCase
#
#
# class TestSetup(APITestCase):
#     pass
#     # def setUp(self):
#     #     self.event = Event.objects.create(title='test title', slug='test-title', description='test event work',
#     #                                             is_active=True, no_of_attendant=20, location='lekki',
#     #                                             link='https://www.google.com', start_date=timezone.now(),
#     #                                             end_date=timezone.now(), image='',)
#     #     self.event.tag.add(['tag1'])
#     #     self.event.attendant.add([self.user2])
#     #     self.event.contact.add([self.user1])
#     #     self.event.created_by.add([self.user1])
#     #     self.event.bit_school.add([self.self.bits_school])
#     #     self.eventList_url = reverse('events')
#     #     self.eventDetails_url = reverse('event', kwargs={'event_id': self.event.id})
#     #     self.galleryList_url = reverse('galleries')
#     #     self.galleryDetails_url = reverse('gallery', kwargs={'event_id': self.event.id})
#     #     self.tagList_url = reverse('tags')
#     #     self.tagDetails_url = reverse('tag', kwargs={'id': self.tag.id})
#     #
#     #     return super().setUp()
#     #
#     # def create_bits_school(self):
#     #     bits_school = BitsSchool.objects.create(name='test-BS')
#     #     return bits_school
#     #
#     # def create_user(self):
#     #     bits_school = self.create_bits_school()
#     #     payload = {"first_name": "jonas101", "last_name": "john", "email": "jonasjohn@gmail.com",
#     #                   "phone_number": "081765443", "password": "password", "bits_school": bits_school,
#     #                   "year_of_graduation": "2026", "country": "AF"}
#     #     payload2 = {"first_name": "femi", "last_name": "debi", "email": "debi@gmail.com",
#     #                 "phone_number": "081765443", "password": "password", "bits_school": bits_school,
#     #                 "year_of_graduation": "2026", "country": "AF"}
#     #
#     #     resp = self.client.post(reverse('signup'), data=payload, format='json')
#     #     resp2 = self.client.post(reverse('signup'), data=payload2, format='json')
#     #     return resp
#     #
#     # def create_tag(self):
#     #     tag = Tag.objects.create(name='test tag')
#     #     return tag
#     #
#     # def create_event(self):
#     #     bits_school = self.create_bits_school()
#     #     tag = self.create_tag()
#     #     user = self.create_user()
#     #     event = Event.objects.create(title='test title', slug='test-title', description='test event work',
#     #                                       is_active=True, no_of_attendant=20, location='lekki',
#     #                                       link='https://www.google.com', start_date=timezone.now(),
#     #                                       end_date=timezone.now(), image='', attendant=user, contant=user,
#     #                                       create_by=user )
#     #     return event
#     #
#     # def tearDown(self):
#     #     return super().tearDown()