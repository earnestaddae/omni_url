import pytest
from urlshortener import utils

from urlshortener import models
pytestmark = pytest.mark.django_db


class TestUtils:
    """Test util functions"""
    def test_default_create_random_code(self):
        key = utils.create_random_url_key()
        assert len(key) == 8

    def test_lengthy_create_random_code(self):
        key = utils.create_random_url_key(12)
        assert len(key) == 12

    def test_create_unique_random_url_key(self):
        url_obj_1 = models.LongURL.objects.create(long_url="https://www.example.com")
        url_obj_2 = models.LongURL.objects.create(long_url="https://www.example.com")
        url_key_1 = utils.create_unique_random_url_key(url_obj_1, 8)
        url_key_2 = utils.create_unique_random_url_key(url_obj_2, 8)
        assert len(url_key_1) == len(url_key_2)
        assert url_key_1 != url_key_2
