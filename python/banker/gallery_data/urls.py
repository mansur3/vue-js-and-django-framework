from django.urls import path
from gallery_data.views import GalleryView, GalleryCategory


urlpatterns = [
    path('', GalleryView.as_view()),
    path('category/', GalleryCategory.as_view())
]