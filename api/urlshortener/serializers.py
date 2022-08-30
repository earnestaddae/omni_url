"""Serializer for the URL model"""

import secrets
from rest_framework import serializers

from urlshortener.models import LongURL

class LongURLSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField()
        
    def get_short_url(self, obj):
        request = self.context["request"]
        url = LongURL.objects.filter(url_key=obj.url_key).first()
        return f'{request.build_absolute_uri("/")}{url.url_key}'
    
    class Meta:
        model = LongURL
        fields = ("long_url", "short_url", "url_key",)
        read_only_fields = ("url_key",)
        
        