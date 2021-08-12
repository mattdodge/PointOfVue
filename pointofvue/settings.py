SETTINGS_PREFIX = "POINT_OF_VUE_"


def get_setting(value, default=None, prefix=True):
    try:
        from django.conf import settings
    except ImportError:
        return default

    if prefix:
        value = SETTINGS_PREFIX + value

    return getattr(settings, value, default)
