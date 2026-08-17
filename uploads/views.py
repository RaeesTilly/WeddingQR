from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Wedding, Photo
from .serializers import WeddingSerializer, PhotoSerializer
from django.shortcuts import render
import qrcode
from io import BytesIO
from django.http import HttpResponse
from .image_processing import optimize_image

@api_view(["GET"])
def wedding_detail(request, slug):
    wedding = get_object_or_404(Wedding, slug=slug)

    serializer = WeddingSerializer(wedding)

    return Response(serializer.data)

@api_view(["POST"])
def photo_upload(request, slug):

    wedding = get_object_or_404(
        Wedding,
        slug=slug
    )

    serializer = PhotoSerializer(
        data=request.data
    )

    if serializer.is_valid():

        photo = serializer.save(
            wedding=wedding
        )

        optimized_image = optimize_image(
            photo.image
        )

        photo.image.save(
            optimized_image.name,
            optimized_image,
            save=True
        )

        return Response(
            PhotoSerializer(photo).data,
            status=201
        )

    return Response(
        serializer.errors,
        status=400
    )

def photo_upload_page(request, slug):
    wedding = get_object_or_404(Wedding, slug=slug)

    if request.method == "POST":

        guest_name = request.POST.get("guest_name", "")

        image = request.FILES.get("image")
        video = request.FILES.get("video")

        if image or video:

            Photo.objects.create(
                wedding=wedding,
                guest_name=guest_name,
                image=image,
                video=video
            )

            return render(
                request,
                "uploads/photo_upload.html",
                {
                    "wedding": wedding,
                    "success": True
                }
            )

    return render(
        request,
        "uploads/photo_upload.html",
        {
            "wedding": wedding
        }
    )

def wedding_gallery(request, slug):
    wedding = get_object_or_404(Wedding, slug=slug)

    photos = wedding.photos.all().order_by("-uploaded_at")

    return render(
        request,
        "uploads/gallery.html",
        {
            "wedding": wedding,
            "photos": photos,
        }
    )

def wedding_home(request, slug):
    wedding = get_object_or_404(Wedding, slug=slug)

    return render(
        request,
        "uploads/wedding_home.html",
        {
            "wedding": wedding
        }
    )

def wedding_qr(request, slug):
    wedding = get_object_or_404(Wedding, slug=slug)

    url = request.build_absolute_uri(
        f"/weddings/{wedding.slug}/"
    )

    qr = qrcode.make(url)

    buffer = BytesIO()
    qr.save(buffer, format="PNG")

    buffer.seek(0)

    return HttpResponse(
        buffer.getvalue(),
        content_type="image/png"
    )

def wedding_qr_card(request, slug):
    wedding = get_object_or_404(Wedding, slug=slug)

    return render(
        request,
        "uploads/qr_card.html",
        {
            "wedding": wedding
        }
    )