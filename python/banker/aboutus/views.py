from django.shortcuts import render, get_object_or_404
from aboutus.models import AboutUsModel
from aboutus.serializers import AboutUsSerializer
from rest_framework import generics, status
from rest_framework.response import Response
import math
# Create your views here.

class AboutUsView(generics.GenericAPIView):
    serializer_class = AboutUsSerializer
    queryset = AboutUsModel.objects.all()

    def get(self, request):
        page_num = int(request.GET.get('page', 1))
        page_limit = int(request.GET.get("limit", 10))

        start_num = (page_num - 1) * page_limit
        end_num = page_num * page_limit

        search_params = request.GET.get("search")

        about_us = AboutUsModel.objects.all()

        total_about_us = about_us.count()

        if search_params:
            about_us = about_us.filter(title__icontains=search_params)
        serializer = self.serializer_class(about_us[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_about_us,
            "page": page_num,
            "last_page": math.ceil(total_about_us / page_limit),
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": {
                    "aboutus": serializer.data
                }
            })
        return Response({
            "status": "fail",
            "message": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    

class AboutUsItemView(generics.GenericAPIView):
    serializer_class = AboutUsSerializer
    def get(self, request, id):        
        about_us_item = AboutUsModel.objects.get(id=id)
        serializer = self.serializer_class(about_us_item)
        try:
            return Response({
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except:
            return Response({
            "status": "fail",
            "message": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

        
