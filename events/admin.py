from django.contrib import admin
from events.models import Event, Tag, EventGallery
from events.forms import GalleryForm

# Register your models here.

admin.site.register(Event)
admin.site.register(Tag)


class GalleryAdmin(admin.ModelAdmin):
    model = EventGallery
    form = GalleryForm

    def save_model(self, request, obj, form, change):
        files = request.FILES.getlist('images')
        for file in files:
            # import pdb
            # pdb.set_trace()
            EventGallery.objects.create(event=obj.event, images=file)
            obj.save()
        super().save_model(request, obj, form, change)


admin.site.register(EventGallery, GalleryAdmin)


# class EventAdmin(admin.ModelAdmin):
#     model = Event
#     inlines = [GalleryAdmin]
#
#     def save_model(self, request, obj, form, change):
#         files = request.FILES.getlist('images')
#         for file in files:
#             import pdb
#             pdb.set_trace()
#             EventGallery.objects.create(event=obj.event, images=file)
#             obj.save()
#         super().save_model(request, obj, form, change)
#
#
# admin.site.register(Event, EventAdmin)
