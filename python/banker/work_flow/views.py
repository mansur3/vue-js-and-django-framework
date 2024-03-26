from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
import math
from work_flow.serializers import WorkFlowItemSerializer, WorkFlowSerializer
from work_flow.models import WorkFlowItemModel, WorkFlowModel


# Create your views here.

class WorkFlowItemView(generics.GenericAPIView):
    serializer_class = WorkFlowItemSerializer
    query_set = WorkFlowItemModel.objects.all()
    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        page_limit = int(request.GET.get("limit", 10))

        start_num = (page_num - 1) * page_limit
        end_num = page_limit * page_num

        search_params = request.GET.get("search")
        work_flow_item_list = WorkFlowItemModel.objects.all()
        total_work_flow_item = work_flow_item_list.count()

        if search_params:
            work_flow_item_list = work_flow_item_list.fitler(title__icontains=search_params)
        serializer = self.serializer_class(work_flow_item_list[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_work_flow_item,
            "page": page_num,
            "last_page" : math.ceil(total_work_flow_item / page_limit),
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": {
                    "work_flow": serializer.data
                }
            }, status=status.HTTP_201_CREATED)
        return Response({
            "status": "fail",
            "message": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)




class WorkFlowView(generics.GenericAPIView):
    serializer_class = WorkFlowSerializer
    query_set = WorkFlowModel.objects.all()

    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        page_limit = int(request.GET.get("limit", 10))

        start_num = (page_num - 1) * page_limit
        end_num = page_limit * page_num

        search_params = request.GET.get("search")

        workFlowList = WorkFlowModel.objects.all()
        total_workflow_count = workFlowList.count()

        if search_params:
            workFlowList = workFlowList.filter(header_title__icontains=search_params)
        serializer = self.serializer_class(workFlowList[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_workflow_count,
            "page": page_num,
            "last_num": math.ceil(total_workflow_count / page_limit),
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
        }, status=status.HTTP_400_BAD_REQUEST)