from django.urls import path
from test_app.views import User, MusicianView, AlbumView

app_name = "test_app"
urlpatterns = [
    path("", User.as_view()),
    path("musician/", MusicianView.as_view()),
    path("album/", AlbumView.as_view())
]