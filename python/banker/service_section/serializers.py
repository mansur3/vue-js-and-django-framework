from rest_framework import serializers
from service_section.models import OurServicesModel


class OurServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurServicesModel
        fields = '__all__'
