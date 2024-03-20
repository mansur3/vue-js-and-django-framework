from django.shortcuts import render

# Create your views here.
from bank.models import BannerModel
from rest_framework.response import Response
from rest_framework import status, generics
from bank.serializers import BannerSerializer
import math
from datetime import datetime


class BannerView(generics.GenericAPIView):
    serializer_class = BannerSerializer
    queryset = BannerModel.objects.all()


    def get(self, request):
        page_num = int(request.GET.get('page', 1))
        limit_num = int(request.GET.get('limit', 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num

        search_params = request.GET.get("search")
        
        banner_list = BannerModel.objects.all()
        total_banner = banner_list.count()

        if search_params:
            banner_list = banner_list.filter(banner_name__icontains=search_params)
        serializer = self.serializer_class(banner_list[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_banner,
            "page": page_num,
            "last_page": math.ceil(total_banner/limit_num),
            "banners": serializer.data
         }, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": {
                    "banners": serializer.data
                }
            }, status=status.HTTP_201_CREATED)
        return Response({
            "status": "fail",
            "message": serializer.errors
        })

    def get_banners(self, pk):
        try:
            return BannerModel.objects.get(pk=pk)
        except:
            return None
    def patch(self, request, pk):
        banner = self.get_banners(pk)
        if banner == None:
            return Response({
                "status": "fail",
                "message": "Banner is not found"
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(banner, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": {
                    "banner": serializer.data
                }
            }, status=status.HTTP_200_OK)
        return Response({
            "status": "fail",
            "message": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        banner = self.get_banners(pk)
        if banner == None:
            return Response({
                "status": "fail",
                "message": "Banner is not found"
            }, status=status.HTTP_404_NOT_FOUND)
        banner.delete()
        return Response({
            "status": "success",
            "message": "Banner has been deleted successfully."
        }, status=status.HTTP_200_OK)