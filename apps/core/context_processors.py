from django.conf import settings


def site_settings(request):
    return {
        "PROJECT_NAME": settings.PROJECT_NAME,
        "SITE_URL": settings.SITE_URL,
        "WHATSAPP_NUMBER": settings.WHATSAPP_NUMBER,
        "CONTACT_EMAIL": settings.CONTACT_EMAIL,
        "MAP_LAT": settings.MAP_LAT,
        "MAP_LNG": settings.MAP_LNG,
        "MAP_ZOOM": settings.MAP_ZOOM,
    }