import django


def get_user_model():
    # Django 1.5+ compatibility
    if django.VERSION >= (1, 8):
        from django.contrib.auth import get_user_model as default_get_user_model
        return default_get_user_model()
    elif django.VERSION >= (1, 5):
        from django.conf import settings
        return settings.AUTH_USER_MODEL
    else:
        from django.contrib.auth.models import User
    return User


def get_user_reference():
    if django.VERSION >= (1, 5):
        from django.conf import settings
        return settings.AUTH_USER_MODEL
    else:
        from django.contrib.auth.models import User
    return User
