from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile


def optimize_image(image_file):

    image = Image.open(image_file)

    # Convert images with transparency to RGB
    if image.mode in ("RGBA", "LA", "P"):
        background = Image.new("RGB", image.size, "white")

        if image.mode == "P":
            image = image.convert("RGBA")

        background.paste(
            image,
            mask=image.getchannel("A")
            if image.mode == "RGBA"
            else None
        )

        image = background

    else:
        image = image.convert("RGB")

    # Maximum dimensions
    max_width = 2000
    max_height = 2000

    image.thumbnail(
        (max_width, max_height),
        Image.Resampling.LANCZOS
    )

    output = BytesIO()

    image.save(
        output,
        format="JPEG",
        quality=85,
        optimize=True
    )

    output.seek(0)

    return ContentFile(
        output.read(),
        name="optimized_photo.jpg"
    )