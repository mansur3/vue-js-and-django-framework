from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from team_member.models import TeamMemberModel
from team_member.serializers import TeamMemberSerializer

# class TeamMemberSerializer(serializers.ModelSerializer):

# Create your views here.

class TeamMemberView(generics.GenericAPIView):
    query_set = TeamMemberModel.objects.all()
    serializer_class = TeamMemberSerializer

    def get(self, request):
        team_members = TeamMemberModel.objects.all()
        serializer = self.serializer_class(team_members, many=True)
        try:
            return Response({
                "status": "success",
                "data": {
                    'team_member': serializer.data
                }
            }, status=status.HTTP_200_OK)
        except:
            return Response({
                "status": "fail",
                "error": 'something went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": {
                    'team_member': serializer.data
                }
            }, status=status.HTTP_201_CREATED)
        return Response({
            'status': 'fail',
            'error': serializer.errors
        })