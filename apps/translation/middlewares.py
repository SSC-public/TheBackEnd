from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
import re


class TranslationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        lang = request.headers['Accept-language'][:2]
        if lang not in ['en', 'fa']:
            lang = 'fa'

        print(lang)

        if hasattr(response, 'data'):
            data = self.translate(response.data, lang)
            r = Response(data)
            r.accepted_renderer = JSONRenderer()
            r.accepted_media_type = "*/*"
            r.renderer_context = {}
            r.render()
            return r
        return response

    def translate(self, data, lang):
        if isinstance(data, dict):
            new_data = {}
            for field in data:
                if re.match('^(.*)_en', field):
                    name = field[:-3]
                    if name + '_fa' in data:
                        new_data[name] = data[name + '_' + lang]
                elif not re.match('^(.*)_fa', field):
                    new_data[field] = self.translate(data[field], lang)
            return new_data
        elif isinstance(data, list):
            new_data = []
            for i in range(len(data)):
                new_data[i] = self.translate(data[i], lang)
            return new_data
        else:
            return data

