from django.urls import path
from testimonial.views import TestimonialViews
urlpatterns = [
    path('', TestimonialViews.as_view())
]