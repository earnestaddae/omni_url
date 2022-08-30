import pytest

from urlshortener import models
pytestmark = pytest.mark.django_db

class TestLongURLModel:
    def test_create_long_url(self):
        instance = models.LongURL.objects.create(
            long_url="https://example.com"
        )
        assert str(instance) == instance.url_key