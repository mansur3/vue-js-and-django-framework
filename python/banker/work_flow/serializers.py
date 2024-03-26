from rest_framework import serializers
from work_flow.models import WorkFlowItemModel, WorkFlowModel

class WorkFlowItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=WorkFlowItemModel
        fields = '__all__'

class WorkFlowSerializer(serializers.ModelSerializer):
    class Meta:
        model=WorkFlowModel
        fields='__all__'

