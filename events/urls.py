from django.urls import path
from events.views import EventListAPI, EventDetailsAPI, GalleryListAPI, GalleryDetailsAPI, TagListAPI,\
    TagDetailsAPI

urlpatterns = [
    path('tags/', TagListAPI.as_view(), name='tags'),
    path('tag/<int:id>/', TagDetailsAPI.as_view(), name='tag'),
    path('events/', EventListAPI.as_view(), name='events'),
    path('event/<str:event_id>/', EventDetailsAPI.as_view(), name='event'),
    path('galleries/', GalleryListAPI.as_view(), name='galleries'),
    path('gallery/<str:event_id>/', GalleryDetailsAPI.as_view(), name='gallery'),
]
