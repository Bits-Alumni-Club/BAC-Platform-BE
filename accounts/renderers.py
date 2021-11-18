from rest_framework import renderers
import json


class UsersRenderers(renderers.JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ''
        if 'ErrorDetails' in str(data):
            response = json.dumps({"errors": data})
        else:
            response = json.dumps({"users": data})
        return response


class UserRegistrationRenderers(renderers.JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ''
        # import pdb
        # pdb.set_trace()
        if 'ErrorDetail' in str(data):
            response = json.dumps({"errors": data})
        else:
            response = json.dumps({"success": data})
        return response


class UserDetailRenderers(renderers.JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ''
        if 'detail' in str(data):
            response = json.dumps({"error": data})
        else:
            response = json.dumps({"user": data})
        return response


class BitsSchoolRenderers(renderers.JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ''
        if 'ErrorDetails' in str(data):
            response = json.dumps({"errors": data})
        else:
            response = json.dumps({"bits_schools": data})
        return response