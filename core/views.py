from django.shortcuts import render
from rest_framework import generics
from core.models import (Page, Home, WhoWeAre, Team, Testimonial, ContactEmail, ContactNumber,
                         Contact, SocialPlatform, FAQ,)
from core.serializers import (PageSerializer, HomeSerializer, TeamSerializer, WhoWeAreSerializer, TestimonySerializer,
                              FAQSerializer, ContactSerializer)
# Create your views here.


class PageAPIView(generics.ListAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class HomeAPIView(generics.ListAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer


class WhoWeAreAPIView(generics.ListAPIView):
    queryset = WhoWeAre.objects.all()
    serializer_class = WhoWeAreSerializer


class TeamAPIView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TestimonialAPIView(generics.ListAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonySerializer


class FAQAPIView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class ContactAPIView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


