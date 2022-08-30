"""Tests for the url_shortener API endpoints"""

import pytest
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from urlshortener.models import LongURL


pytestmark = pytest.mark.django_db

CREATE_URL_SHORTENER_URL = reverse('urlshortener:create')
# RETRIEVE_URL_SHORTENER_URL = reverse('urlshortner:retrieve')


class TestPublicUrlShortnerAPI:
    """Tests for creating short urls"""
    
    def test_create_short_url_successfully(self, client: APIClient):
        """Test creating a new short url"""
        payload = {
            'long_url': "https://www.iamlongurl/long-url-enough-to-make-short"
        }
        response = client.post(CREATE_URL_SHORTENER_URL, data=payload)
        assert response.status_code == status.HTTP_201_CREATED
        url_exists = LongURL.objects.filter(long_url=payload['long_url']).exists()
        assert url_exists
        