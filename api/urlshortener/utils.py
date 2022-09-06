import secrets
import string


def create_random_url_key(length=8):
    """Generates a random key as url_key"""
    chars = string.ascii_letters + string.digits
    return "".join(secrets.choice(chars) for _ in range(length))


def create_unique_random_url_key(obj, length):
    """Generates a unique random key for the same long_url objects"""
    random_url_key = create_random_url_key(length)
    model_class = obj.__class__
    while model_class.objects.filter(url_key=random_url_key).exists():
        random_url_key = create_random_url_key(length) 
    return random_url_key
