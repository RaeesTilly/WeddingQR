from django.urls import path

from .views import (
    wedding_detail,
    photo_upload,
    wedding_qr,
)

urlpatterns = [
    path(
        "weddings/<slug:slug>/",
        wedding_detail,
        name="wedding-detail",
    ),

    path(
        "weddings/<slug:slug>/photos/",
        photo_upload,
        name="photo-upload",
    ),

    path(
        "weddings/<slug:slug>/qr/",
        wedding_qr,
        name="wedding-qr",
    ),
]