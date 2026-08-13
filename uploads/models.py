from django.db import models

class Wedding(models.Model):
    bride_name = models.CharField(max_length = 100)
    groom_name = models.CharField(max_length = 100)
    wedding_date = models.DateField()
    venue = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.bride_name} & {self.groom_name}'
    
class Photo(models.Model):

    wedding = models.ForeignKey(
        Wedding,
        on_delete=models.CASCADE,
        related_name="photos"
    )

    guest_name = models.CharField(
        max_length=100,
        blank=True
    )

    image = models.ImageField(
        upload_to="photos/",
        blank=True,
        null=True
    )

    video = models.FileField(
        upload_to="videos/",
        blank=True,
        null=True
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.guest_name or 'Anonymous'} - {self.wedding}"