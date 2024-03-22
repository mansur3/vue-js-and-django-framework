from django.shortcuts import render

# Create your views here.
from service.models import  ServiceModel, ServiceItem
from service.serializers import ServiceSerializer, ServiceItemSerializer
from rest_framework import generics, status
from rest_framework.response import Response
import math

class ServiceView(generics.GenericAPIView):
    serializer_class = ServiceSerializer
    queryset = ServiceModel.objects.all()

    def get(self, request):
        page_num = int(request.GET.get('page', 1))
        page_limit = int(request.GET.get('limit', 10))
        start_num = (page_num - 1) * page_limit
        end_num = page_limit * page_num

        search_params = request.GET.get('search')

        service_list = ServiceModel.objects.all()
        total_service_count = service_list.count()

        if search_params:
            service_list = service_list.filter(title__icontains=search_params)
        serializer = self.serializer_class(service_list[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_service_count,
            "page": page_num,
            "last_page": math.ceil(total_service_count / page_limit),
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
    # def get(self, request, pk):
    #     list = ServiceModel.objects.get(pk=pk)

    #     if list:
    #         return Response({
    #             "status": "success",
    #             "data": self.serializer_class(list)
    #         }, status=status.HTTP_200_OK)
    #     return Response({
    #         "status": "fail",
    #         "message": "Something went wrong"
    #     })

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

    def get_one_service(self, pk):
        service = ServiceModel.objects.get(pk=pk)
        if service:
            return service
        return None
    
    def patch(self, request, pk):
        service = self.get_one_service(pk)
        if service == None:
            return Response({
                "status": "fail",
                "message": "Service not found."
            }, status = status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(service, data=request.data, partial=True )
        if serializer.is_valid():
            return Response({
                "status": "success",
                "data": {
                    "service": serializer.data
                }
            }, status=status.HTTP_200_OK)
        return Response({
            "status": "fail",
            "message": serializer.errors
        }, status = status.HTTP_400_BAD_REQUEST)
    def delete(self, pk):
        service = self.get_one_service(pk)
        if service == None:
            return Response({
                "status": "fail",
                "message": "Service not found"
            }, status=status.HTTP_404_NOT_FOUND)
        service.delete()
        return Response({
            "status": "success",
            "message": "Service is deleted successfully."
        }, status=status.HTTP_200_OK)

# class DescriptionItemView(generics.GenericAPIView):
#     serializer_class = ServiceDescriptionItemSerializer
#     queryset = DescriptionItemModel.objects.all()

#     def get(self, request):
#         page_num = int(request.GET.get('page', 1))
#         page_limit = int(request.GET.get('limit', 10))
#         start_num = (page_num - 1) * page_limit
#         end_num = page_limit * page_num

#         search_params = request.GET.get('search')

#         service_list = DescriptionItemModel.objects.all()
#         total_service_count = service_list.count()

#         if search_params:
#             service_list = service_list.filter(title__icontains=search_params)
#         serializer = self.serializer_class(service_list[start_num:end_num])
        
#         return Response({
#             "status": "success",
#             "total": total_service_count,
#             "page": page_num,
#             "last_page": math.ceil(total_service_count / page_limit),
#             "data": serializer.data
#         }, status=status.HTTP_200_OK)

    
#     # def get(self, request, pk):
#     #     list = DescriptionItemModel.objects.get(pk=pk)

#     #     if list:
#     #         return Response({
#     #             "status": "success",
#     #             "data": self.serializer_class(list)
#     #         }, status=status.HTTP_200_OK)
#     #     return Response({
#     #         "status": "fail",
#     #         "message": "Something went wrong"
#     #     })

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             return Response({
#                 "status": "success",
#                 "data": {
#                     "banners": serializer.data
#                 }
#             }, status=status.HTTP_201_CREATED)
#         return Response({
#             "status": "fail",
#             "message": serializer.errors
#         })

#     def get_one_service(self, pk):
#         service = DescriptionItemModel.objects.get(pk=pk)
#         if service:
#             return service
#         return None
    
#     def patch(self, request, pk):
#         service = self.get_one_service(pk)
#         if service == None:
#             return Response({
#                 "status": "fail",
#                 "message": "Service not found."
#             }, status = status.HTTP_404_NOT_FOUND)
#         serializer = self.serializer_class(service, data=request.data, partial=True )
#         if serializer.is_valid():
#             return Response({
#                 "status": "success",
#                 "data": {
#                     "service": serializer.data
#                 }
#             }, status=status.HTTP_200_OK)
#         return Response({
#             "status": "fail",
#             "message": serializer.errors
#         }, status = status.HTTP_400_BAD_REQUEST)
#     def delete(self, pk):
#         service = self.get_one_service(pk)
#         if service == None:
#             return Response({
#                 "status": "fail",
#                 "message": "Service not found"
#             }, status=status.HTTP_404_NOT_FOUND)
#         service.delete()
#         return Response({
#             "status": "success",
#             "message": "Service is deleted successfully."
#         }, status=status.HTTP_200_OK)


class ServiceItemView(generics.GenericAPIView):
    serializer_class = ServiceItemSerializer
    queryset = ServiceItem.objects.all()

    def get(self, request):
        page_num = int(request.GET.get('page', 1))
        page_limit = int(request.GET.get('limit', 10))
        start_num = (page_num - 1) * page_limit
        end_num = page_limit * page_num

        search_params = request.GET.get('search')

        service_list = ServiceItem.objects.all()
        total_service_count = service_list.count()

        if search_params:
            service_list = service_list.filter(title__icontains=search_params)
        serializer = self.serializer_class(service_list[start_num:end_num], many=True)
       
        return Response({
            "status": "success",
            "total": total_service_count,
            "page": page_num,
            "last_page": math.ceil(total_service_count / page_limit),
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
    # def get(self, request, pk):
    #     list = ServiceItem.objects.get(pk=pk)

    #     if list:
    #         return Response({
    #             "status": "success",
    #             "data": self.serializer_class(list)
    #         }, status=status.HTTP_200_OK)
    #     return Response({
    #         "status": "fail",
    #         "message": "Something went wrong"
    #     })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
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

    def get_one_service(self, pk):
        service = ServiceItem.objects.get(pk=pk)
        if service:
            return service
        return None
    
    def patch(self, request, pk):
        service = self.get_one_service(pk)
        if service == None:
            return Response({
                "status": "fail",
                "message": "Service not found."
            }, status = status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(service, data=request.data, partial=True )
        if serializer.is_valid():
            return Response({
                "status": "success",
                "data": {
                    "service": serializer.data
                }
            }, status=status.HTTP_200_OK)
        return Response({
            "status": "fail",
            "message": serializer.errors
        }, status = status.HTTP_400_BAD_REQUEST)
    def delete(self, pk):
        service = self.get_one_service(pk)
        if service == None:
            return Response({
                "status": "fail",
                "message": "Service not found"
            }, status=status.HTTP_404_NOT_FOUND)
        service.delete()
        return Response({
            "status": "success",
            "message": "Service is deleted successfully."
        }, status=status.HTTP_200_OK)
 