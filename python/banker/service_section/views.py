from django.shortcuts import render
from service_section.models import OurServicesModel
from service_section.serializers import OurServiceSerializer
from rest_framework import generics, status
from rest_framework.response import Response
import math

# Create your views here.

class ServiceSectionView(generics.GenericAPIView):
    serializer_class = OurServiceSerializer
    query_set = OurServicesModel.objects.all()

    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        page_limit = int(request.GET.get("limit", 10))

        start_num = (page_num - 1) * page_limit
        end_num = page_limit * page_num

        search_params = request.GET.get('search')

        service_section_list = OurServicesModel.objects.all()
        total_service_section_count = service_section_list.count()
        
        if search_params:
            service_section_list = service_section_list.filter(title__icontains=search_params)
        serializer = self.serializer_class(service_section_list[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_service_section_count,
            "page": page_num,
            "last_page": math.ceil(total_service_section_count / page_limit),
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": 'success',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "status": "fail",
            "message": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)