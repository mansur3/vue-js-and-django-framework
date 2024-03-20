from django.urls import path
from service.views import ServiceView, ServiceItemView
# , DescriptionItemView, 
urlpatterns = [
    path('', ServiceView.as_view()),
    # path("<int:pk>/", ServiceView.as_view()),
    # path("service-description/", DescriptionItemView.as_view())
    path("service-item/", ServiceItemView.as_view())
]