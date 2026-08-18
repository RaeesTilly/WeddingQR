from django.urls import path

from .views import (
    wedding_home,
    photo_upload_page,
    wedding_gallery,
    wedding_qr,
    wedding_qr_card,
)

urlpatterns = [
    path(
        "weddings/<slug:slug>/",
        wedding_home,
        name="wedding-home",
    ),

    path(
        "weddings/<slug:slug>/upload/",
        photo_upload_page,
        name="photo-upload",
    ),

    path(
        "weddings/<slug:slug>/gallery/",
        wedding_gallery,
        name="wedding-gallery",
    ),

    path(
        "weddings/<slug:slug>/qr/",
        wedding_qr,
        name="wedding-qr",
    ),

    path(
        "weddings/<slug:slug>/qr-card/",
        wedding_qr_card,
        name="wedding-qr-card",
    ),
]