from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics
from user.models import UserModel
from user.serializers import UserSerializer

# Create your views here.


class UserView(generics.GenericAPIView):
    serializer_class = UserSerializer
    query_set = UserModel.objects.all()
    def get(self, request):
        user_list = UserModel.objects.all()
        serializer = self.serializer_class(user_list, many=True)
        return Response({
            "status": "success",
            "data": serializer.data
        }, status = status.HTTP_200_OK)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data
            }, status = status.HTTP_201_CREATED)
        return Response({
            "status": "success",
            "message": serializer.errors
        }, status = status.HTTP_400_BAD_REQUEST)