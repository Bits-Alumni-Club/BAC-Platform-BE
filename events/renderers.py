from rest_framework import renderers
import json


class EventsRenderers(renderers.JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ''
        if 'ErrorDetails' in str(data):
            response = json.dumps({"errors": data})
        else:
            response = json.dumps({"events": data})
        return response


class EventDetailRenderers(renderers.JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ''
        if 'detail' in str(data):
            response = json.dumps({"error": data})
        else:
            response = json.dumps({"event": data})
        return response


class GalleriesRenderers(renderers.JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ''
        if 'ErrorDetails' in str(data):
            response = json.dumps({"errors": data})
        else:
            response = json.dumps({"galleries": data})
        return response


class GalleryDetailRenderers(renderers.JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ''
        if 'detail' in str(data):
            response = json.dumps({"error": data})
        else:
            response = json.dumps({"gallery": data})
        return response


class TagsRenderers(renderers.JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ''
        if 'ErrorDetails' in str(data):
            response = json.dumps({"errors": data})
        else:
            response = json.dumps({"tags": data})
        return response


class TagDetailRenderers(renderers.JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ''
        if 'detail' in str(data):
            response = json.dumps({"error": data})
        else:
            response = json.dumps({"tag": data})
        return response

# class BitsSchoolRenderers(renderers.JSONRenderer):
#     charset = 'utf-8'
#
#     def render(self, data, accepted_media_type=None, renderer_context=None):
#         response = ''
#         if 'ErrorDetails' in str(data):
#             response = json.dumps({"errors": data})
#         else:
#             response = json.dumps({"bits_schools": data})
#         return response