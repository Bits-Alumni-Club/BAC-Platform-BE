from django.urls import path
from core.views import (PageAPIView, HomeAPIView, TeamAPIView, WhoWeAreAPIView, TestimonialAPIView, FAQAPIView,
                        ContactAPIView)


urlpatterns = [
    path('page/', PageAPIView.as_view(), name='page'),
    path('home/', HomeAPIView.as_view(), name='home'),
    path('teams/', TeamAPIView.as_view(), name='teams'),
    path('who-we-are/', WhoWeAreAPIView.as_view(), name='wwa'),
    path('testimonials/', TestimonialAPIView.as_view(), name='testimonials'),
    path('faq/', FAQAPIView.as_view(), name='faq'),
    path('contacts/', ContactAPIView.as_view(), name='contacts'),

]