from contact_us.models import ContactUsModel
from rest_framework import serializers

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUsModel
        fields = "__all__"