from events.models import Event, Tag, EventGallery
from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name", "created_at", "updated_at")


class EventSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=True)

    class Meta:
        model = Event
        fields = ("id", "event_id", "title", "description", "slug", "location",
                  "start_date", "end_date", "image", "tag", "is_gallery", "created_at", "updated_at")
        lookup_field = ['event_id']


class EventGallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = EventGallery
        fields = ('id', 'event', 'images')


class GallerySerializer(serializers.ModelSerializer):
    # galleries = serializers.StringRelatedField(many=True)
    galleries = EventGallerySerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ("id", "event_id", "title", "description", "slug", "location",
                  "start_date", "end_date", "image", "galleries", "tag", "is_gallery",
                  "created_at", "updated_at")
        lookup_field = ['event_id']


