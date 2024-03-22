from django.urls import path
from aboutus.views import AboutUsView, AboutUsItemView

urlpatterns = [
    path('', AboutUsView.as_view()),
    path('<int:id>/', AboutUsItemView.as_view())
]

