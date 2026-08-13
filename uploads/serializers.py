from rest_framework import serializers
from .models import Wedding, Photo

class WeddingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wedding
        fields = "__all__"

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = [
            "id", 
            "wedding",
            "guest_name",
            "image",
            "video", 
            "uploaded_at",
        ]
        read_only_fields = [
            "id",
            "weddng",
            "uploaded_at",
        ]

    def validate_image(self, image):
        max_size = 20 * 1024 * 1024

        if image.size > max_size:
            raise serializers.ValidationError(
                "image must be smaller than 20 MB."
            )

        return image

    def validate_video( self, video):
        max_size = 100 * 1024 * 1024

        if video.size > max_size:
            raise serializers.ValidationError(
                "video must be smaller than 100 MB."
            )

        allowed_types = [
            "video/mp4",
            "video/quicktime",
            "video.webm",
        ]

        if video.content_type not in allowed_types:
            raise serializers.ValidationError(
                "only MP4, MOV, and WebM videos are allowed."
            )
        return video 