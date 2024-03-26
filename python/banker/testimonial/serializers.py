from testimonial.models import TestimonialModel
from rest_framework import serializers


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestimonialModel
        fields = '__all__'