from django.conf import settings


def vars(request):
    # return the value you want as a dictionnary.
    # you may add multiple values in there.
    return {
        'PROTOCOL': settings.PROTOCOL,
        'BASE_URL': settings.BASE_URL,
        'BASE_URL_TRIM': settings.BASE_URL_TRIM,
        'CLIENT_URL': settings.CLIENT_URL,
        'STATIC_URL': settings.STATIC_URL,
        'STATIC_IMG_URL': settings.STATIC_IMG_URL,
        'MEDIA_URL': settings.MEDIA_URL,
        'DEFAULT_META': settings.DEFAULT_META
    }
