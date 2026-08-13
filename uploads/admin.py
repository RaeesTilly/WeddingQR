from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Wedding, Photo


@admin.register(Wedding)
class WeddingAdmin(admin.ModelAdmin):

    list_display = (
        "bride_name",
        "groom_name",
        "wedding_date",
        "venue",
        "qr_code_link",
        "qr_card_link",
    )

    prepopulated_fields = {
        "slug": ("bride_name", "groom_name"),
    }

    def qr_code_link(self, obj):
        url = reverse(
            "wedding-qr",
            kwargs={"slug": obj.slug}
        )

        return format_html(
            '<a href="{}" target="_blank">View QR Code</a>',
            url
        )

    qr_code_link.short_description = "QR Code"

    def qr_card_link(self, obj):
        url = reverse(
            "wedding-qr-card",
            kwargs={"slug": obj.slug}
        )

        return format_html(
            '<a href="{}" target="_blank">Print QR Card</a>',
            url
        )

    qr_card_link.short_description = "QR Card"


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):

    list_display = (
        "guest_name",
        "wedding",
        "media_type",
        "media_preview",
        "uploaded_at",
    )

    list_filter = (
        "wedding",
        "uploaded_at",
    )

    search_fields = (
        "guest_name",
        "wedding__bride_name",
        "wedding__groom_name",
    )

    def media_type(self, obj):

        if obj.video:
            return "🎥 Video"

        if obj.image:
            return "📸 Photo"

        return "Unknown"

    media_type.short_description = "Media"

    def media_preview(self, obj):

        if obj.image:
            return format_html(
                '''
                <img
                    src="{}"
                    style="
                        width:100px;
                        height:100px;
                        object-fit:cover;
                        border-radius:8px;
                    "
                />
                ''',
                obj.image.url
            )

        if obj.video:
            return format_html(
                '''
                <video
                    width="160"
                    height="100"
                    controls
                    style="border-radius:8px;"
                >
                    <source src="{}">
                    Your browser does not support video.
                </video>
                ''',
                obj.video.url
            )

        return "No media"

    media_preview.short_description = "Preview"