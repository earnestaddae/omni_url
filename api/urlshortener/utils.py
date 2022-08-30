import secrets
import string

def create_random_url_key(length=8):
    chars = string.ascii_letters + string.digits
    return "".join(secrets.choice(chars) for _ in range(length))

def create_unique_random_url_key(obj):
    random_url_key = create_random_url_key()
    model_class = obj.__class__
    if model_class.objects.filter(url_key=random_url_key).exists():
        return create_unique_random_url_key()
    return random_url_key