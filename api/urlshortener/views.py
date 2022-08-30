"""Views for the URL API"""

from rest_framework import generics
from urlshortener.serializers import LongURLSerializer


class CreateShortURLView(generics.CreateAPIView):
    serializer_class = LongURLSerializer