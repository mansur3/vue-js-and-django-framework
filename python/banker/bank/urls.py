from django.urls import path, include
from bank.views import BannerView
app_name = "bank"
urlpatterns=[
    path("", BannerView.as_view())
]