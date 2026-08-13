from django.urls import path

from .views import wedding_home


urlpatterns = [
    path(
        "<slug:slug>/",
        wedding_home,
        name="wedding-home",
    ),
]