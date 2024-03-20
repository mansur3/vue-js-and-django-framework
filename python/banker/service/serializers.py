from rest_framework import serializers

from service.models import ServiceModel, ServiceItem

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=ServiceModel
        fields = '__all__'
class ServiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=ServiceItem
        fields = '__all__'

# class ServiceDescriptionItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=DescriptionItemModel
#         fields='__all__'
# class ItemDescriptionModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ItemDescriptionModel
#         fields='__all__'
