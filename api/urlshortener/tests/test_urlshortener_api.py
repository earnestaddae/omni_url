"""Tests for the url_shortener API endpoints"""

import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from urlshortener.models import LongURL


pytestmark = pytest.mark.django_db

CREATE_URL_SHORTENER_URL = reverse('urlshortener:create')


def urlshortener_detail_url(urlshortener_url_key):
    return reverse("urlshortener:redirect", kwargs=dict(url_key=urlshortener_url_key))


class TestPublicUrlShortnerAPI:
    """Tests for creating short urls"""
    def test_create_short_url_successfully(self, client: APIClient):
        payload = {
            'long_url': "https://www.iamlongurl/long-url-enough-to-make-short"
        }
        response = client.post(CREATE_URL_SHORTENER_URL, data=payload)
        assert response.status_code == status.HTTP_201_CREATED
        url_exists = LongURL.objects.filter(long_url=payload['long_url']).exists()
        assert url_exists
        assert "url_key" in response.json()

    def test_create_short_url_with_same_long_url(self, client: APIClient):
        url_obj = LongURL.objects.create(long_url="https://www.example.com")
        payload = {
            "long_url": "https://www.example.com"
        }
        response = client.post(CREATE_URL_SHORTENER_URL, data=payload)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()['long_url'] == url_obj.long_url
        assert response.json()['long_url'] == payload['long_url']
        assert response.json()['url_key'] != url_obj.url_key

    def test_retrieve_url(self, client: APIClient):
        long_url = 'http://www.example.com'
        url_obj = LongURL.objects.create(long_url=long_url)
        url = urlshortener_detail_url(url_obj.url_key)
        response = client.get(url)
        assert response.status_code == status.HTTP_302_FOUND

    def test_post_url_retrieve_not_allowed(self, client: APIClient):
        long_url = 'http://www.example.com'
        url_obj = LongURL.objects.create(long_url=long_url)
        url = urlshortener_detail_url(url_obj.url_key)
        response = client.post(url, data={})
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
