from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static


def home(request):
    return redirect("/wedding/weddings/Tasmiyah-Mohammed/")


urlpatterns = [
    path("", home, name="home"),

    path("admin/", admin.site.urls),

    # API URLs
    path("api/", include("uploads.urls")),

    # Public wedding website
    path("wedding/", include("uploads.public_urls")),
]


# Serve uploaded media files
# This allows images/videos to work on Render as well.
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)