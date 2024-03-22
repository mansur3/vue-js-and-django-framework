from django.urls import path
from gallery.views import GalleryView, GalleryCategory


urlpatterns = [
    path('', GalleryView.as_view()),
    path('category/', GalleryCategory.as_view())
]