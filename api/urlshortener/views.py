"""Views for the URL API"""

from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from urlshortener.models import LongURL
from urlshortener.serializers import LongURLSerializer


class CreateShortURLView(generics.CreateAPIView):
    """Creates a short url from long_url"""
    serializer_class = LongURLSerializer


class RedirectShortURLView(generics.RetrieveAPIView):
    """Retrieves and redirects to long_url based on url_key"""
    queryset = LongURL.objects.all()
    serializer_class = LongURLSerializer
    lookup_field = "url_key"

    def retrieve(self, *args, **kwargs):
        url_key = kwargs.get('url_key')
        try:
            instance = LongURL.objects.get(url_key=url_key)
            return redirect(instance.long_url)
        except LongURL.DoesNotExist:
            return Response({"error": "That url does not exist"}, status=status.HTTP_404_NOT_FOUND)
