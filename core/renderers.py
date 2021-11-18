from rest_framework import renderers
import json


class HomeRenderers(renderers.JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ''
        if 'ErrorDetails' in str(data):
            response = json.dumps({"errors": data})
        else:
            response = json.dumps({"Home": data})
        return response
