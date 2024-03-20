from rest_framework import serializers

from bank.models import BannerModel

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerModel
        fields = '__all__'
