from django.shortcuts import render
from events.models import Event, Tag, EventGallery
from events.serializers import EventSerializer, GallerySerializer, TagSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from events.utils import EventSearchFilter
from events.renderers import (EventsRenderers, EventDetailRenderers, GalleriesRenderers, GalleryDetailRenderers,
                              TagsRenderers, TagDetailRenderers)


# from rest_framework import filters
# Create your views here.


class TagListAPI(generics.ListAPIView):
    renderer_classes = (TagsRenderers,)

    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetailsAPI(generics.RetrieveAPIView):
    renderer_classes = (TagDetailRenderers,)

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'id'


class EventListAPI(generics.ListAPIView):
    # permission_classes = (IsAuthenticated,)
    renderer_classes = (EventsRenderers,)

    filter_backends = (EventSearchFilter,)
    queryset = Event.objects.filter(is_gallery=False)
    serializer_class = EventSerializer
    # http://127.0.0.1:8000/events?search=art&search_fields=title
    # http://127.0.0.1:8000/events?search=educations&search_fields=tag__name


class EventDetailsAPI(generics.RetrieveAPIView):
    renderer_classes = (EventDetailRenderers,)

    # permission_classes = (IsAuthenticated,)
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    lookup_field = 'event_id'


class GalleryListAPI(generics.ListAPIView):
    renderer_classes = (GalleriesRenderers,)

    serializer_class = GallerySerializer
    queryset = Event.objects.filter(is_gallery=True)


class GalleryDetailsAPI(generics.RetrieveAPIView):
    renderer_classes = (GalleryDetailRenderers,)

    serializer_class = GallerySerializer
    queryset = Event.objects.filter(is_gallery=True)
    lookup_field = 'event_id'
