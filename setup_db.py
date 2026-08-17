import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

django.setup()

from uploads.models import Wedding

if not Wedding.objects.filter(slug="Tasmiyah-Mohammed").exists():
    Wedding.objects.create(
        bride_name="Tasmiyah",
        groom_name="Mohammed",
        wedding_date="2026-10-11",
        venue="Anees, Glass hall",
        slug="Tasmiyah-Mohammed",
    )

print("Wedding database setup complete.")