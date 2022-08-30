from django.db import models


class LongURL(models.Model):
    long_url = models.URLField()
    short_url = models.URLField(max_length=100, unique=True)
    url_key = models.CharField(max_length=10, help_text="key to the long url", unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['url_key'], name='url_key_index'),
        ]
