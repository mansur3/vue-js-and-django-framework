from django.urls import path
from service_section.views import ServiceSectionView

urlpatterns = [
    path('', ServiceSectionView.as_view())
]