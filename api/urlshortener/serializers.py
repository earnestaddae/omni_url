"""Serializer for the URL model"""

import secrets
from rest_framework import serializers

from urlshortener.models import LongURL

class LongURLSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LongURL
        fields = ("long_url", "short_url",)
        read_only_fields = ("short_url",)
        
    def create(self, validated_data):
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        url_key = ''.join(secrets.choice(chars) for _ in range(8))
        short_url = f'https://omnihr.url/{url_key}'
        long_url = validated_data.get('long_url')
        data = dict(url_key=url_key, short_url=short_url, long_url=long_url)
        return LongURL.objects.create(**data)
        
        