from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics
from testimonial.models import TestimonialModel
from testimonial.serializers import TestimonialSerializer

import math
# Create your views here.

class TestimonialViews(generics.GenericAPIView):
    serializer_class = TestimonialSerializer
    query_set = TestimonialModel.objects.all()
    def get(self, request):
        page_num = int(request.GET.get('page', 1))
        page_limit = int(request.GET.get('limit', 10))

        start_num = (page_num - 1) * page_limit
        end_num = page_limit * page_num

        search_params = request.GET.get("search")

        testimonial_list = TestimonialModel.objects.all()
        total_testimonial_list_count = testimonial_list.count()

        if search_params:
            testimonial_list = testimonial_list.filter(subject__icontains=search_params)
        serializer = self.serializer_class(testimonial_list[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_testimonial_list_count,
            "page": page_num,
            "last_page": math.ceil(total_testimonial_list_count / page_limit),
            "data": serializer.data

        }, status=status.HTTP_200_OK)
    def post(self, request):
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
        }, status = status.HTTP_400_BAD_REQUEST)
    
    