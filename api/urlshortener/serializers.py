"""Serializer for the URL model"""

from rest_framework import serializers
from urlshortener.models import LongURL


class LongURLSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField()

    def get_short_url(self, obj):
        request = self.context["request"]
        return f'{request.build_absolute_uri("/")}{obj.url_key}'

    class Meta:
        model = LongURL
        fields = ("long_url", "short_url", "url_key",)
        read_only_fields = ("url_key",)
