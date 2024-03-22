from django.shortcuts import render
from gallery.models import GalleryCategoryModel, GalleryModel
from rest_framework import generics, status
from rest_framework.response import Response
from gallery.serializers import GallerySerializer, GalleryCategorySerializer
# Create your views here.

class GalleryView(generics.GenericAPIView):
    query_set = GalleryModel.objects.all()
    serializer_class = GallerySerializer

    def get(self, request):
        gallery_view = GalleryModel.objects.all()
        serializer = self.serializer_class(gallery_view, many=True)
        try:
            return Response({
                'status': "success",
                'data': {
                    'gallery': serializer.data
                }
            })
        except:
            return Response({
                "status": "fail",
                "message": "Something went wrong"
            }, status=status.HTTP_400_BAD_REQUEST)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': "success",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'status': "fail",
            'message': serializer.errors
        }, status = status.HTTP_400_BAD_REQUEST)


class GalleryCategory(generics.GenericAPIView):
    query_set = GalleryCategoryModel.objects.all()
    serializer_class = GalleryCategorySerializer

    def get(self, request):
        gallery_view = GalleryCategoryModel.objects.all()
        serializer = self.serializer_class(gallery_view, many=True)
        try:
            return Response({
                'status': "success",
                'data': {
                    'gallery': serializer.data
                }
            })
        except:
            return Response({
                "status": "fail",
                "message": "Something went wrong"
            }, status=status.HTTP_400_BAD_REQUEST)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': "success",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'status': "fail",
            'message': serializer.errors
        }, status = status.HTTP_400_BAD_REQUEST)


