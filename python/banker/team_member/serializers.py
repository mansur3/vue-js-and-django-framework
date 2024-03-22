from rest_framework import serializers

from team_member.models import TeamMemberModel

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMemberModel
        fields = '__all__'