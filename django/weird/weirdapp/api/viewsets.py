import urllib

from django.http import HttpResponse
from rest_framework import views
from weirdapp import weird_text

class EncodeViewSet(views.APIView):
    def get(self, request):
        data = request._request.environ['QUERY_STRING']
        data = urllib.parse.unquote(data)
        try:
            e = weird_text.Encoder(data)
            encoded_string = e.encode_string()
        except ValueError:
            return HttpResponse(status=400)
        return HttpResponse(encoded_string, content_type="application/vnd.api+json", status=200)


class DecodeViewSet(views.APIView):
    def get(self, request):
        data = request._request.environ['QUERY_STRING']
        data = urllib.parse.unquote(data)
        try:
            d = weird_text.Decoder(data)
            decoded_string = d.decode_string()
        except ValueError:
            return HttpResponse(status=400)
        return HttpResponse(decoded_string, content_type="application/vnd.api+json", status=200)


