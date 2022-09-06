from django.db import models
from urlshortener import utils


class LongURL(models.Model):
    long_url = models.URLField(blank=False, null=False)
    url_key = models.CharField(max_length=10, help_text="key to the long url", unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.url_key:
            self.url_key = utils.create_unique_random_url_key(self, 8)
        super().save(*args, **kwargs)

    class Meta:
        indexes = [
            models.Index(fields=['url_key'], name='url_key_index'),
        ]

    def __str__(self):
        return self.url_key
