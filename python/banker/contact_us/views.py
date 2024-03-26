from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response

from contact_us.serializers import ContactUsSerializer
from contact_us.models import ContactUsModel

# Create your views here.

class ContactUsView(generics.GenericAPIView):
    serializer_class = ContactUsSerializer
    query_set = ContactUsModel.objects.all()

    def get(self, request):
        data = ContactUsModel.objects.all()
        serializer = self.serializer_class(data, many=True)
        return Response({ 
            "status": "success",
            "data": serializer.data
        }, status=status.HTTP_200_OK)



    def post(self, request):
        print('test', request.method, request.path,  request.body, request.data, request.headers)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "status": "fail",
            "message": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


