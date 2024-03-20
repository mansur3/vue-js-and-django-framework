from django.shortcuts import render
from django.http import HttpResponse
from test_app.models import UserModel, Musician, Album, Person, Fruit
from rest_framework.response import Response
from rest_framework import status, generics
from test_app.serializers import UserSerializer, MusicianSerializer, AlbumSerializer, PersonSerializer, FruitSerializer
import math
from datetime import datetime

# Create your views here.
# def index(request):
#     response = "Take me down to the river bend. Take me down to the fighting end. Wash the poison from of my skin. Show me how to be whole again. Fly me up in the silver wing. Past the black where siren sing. After the night when i wake up i will see what tomorrow  bring."
#     return HttpResponse(response)
#CRUD User
# def create_user(request):

class MusicianView(generics.GenericAPIView):
    serializer_class = MusicianSerializer
    queryset = Musician.objects.all()

    def get(self, request):
        page_num = int(request.GET.get('page', 1))
        limit_num = int(request.GET.get('limit', 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num

        search_param = request.GET.get("search")

        musicians = Musician.objects.all()
        total_musicians = musicians.count()
        if search_param:
            musicians = musicians.filter(first_name__icontains=search_param)
        serializer = self.serializer_class(musicians[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_musicians,
            "page": page_num,
            "last_page": math.ceil(total_musicians / limit_num),
            "musicians": serializer.data
        })
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": {
                    "musicians": serializer.data
                }
            }, status = status.HTTP_201_CREATED)
        else:
            return Response({
                "status": "fail",
                "message": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    def get_musicians(self, pk):
        try:
            return Musician.objects.filter(pk=pk)
        except:
            return None

    def patch(self, request, pk):
        check_is_valid_musician = self.get_musicians(self, pk)
        if check_is_valid_musician == None:
            return Response({
                "status": "fail",
                "message": "Musician not found"
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(check_is_valid_musician, data=request.data, partitial=True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({
                "status": "success",
                "data": {
                    "musician": serializer.data
                }
            }, status=status.HTTP_200_OK)
        return Response({
            "status": "fail",
            "message": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        musician = self.get_musicians(self, pk)
        if musician == None:
            return Response({
                "status": "fail",
                "message": "Musician is not found."
            }, status=status.HTTP_404_NOT_FOUND)
        musician.delete()
        return Response({
            "status": "success",
            "message": "Musician has been deleted."
        }, status = status.HTTP_204_NO_CONTENT)


class AlbumView(generics.GenericAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    
    def get(self, request):
        # pagination
        page_num = int(request.GET.get('page', 1))
        limit_num = int(request.GET.get('limit', 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num

        # search params
        search_params = request.GET.get('search')
        album =  Album.objects.all()
        total_results = album.count()
        if search_params:
            album = album.filter(name__icontains=search_params)
        serializer = self.serializer_class(album[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_results,
            "page": page_num,
            "last_page": math.ceil(total_results / limit_num),
            'album': serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response({
                "status": "success",
                "data": {
                    "album": serializer.data
                }
            }, status=status.HTTP_201_CREATED)
        return Response({
            "status": "fail",
            "message": "Album is not found"
        }, status=status.HTTP_400_BAD_REQUEST)

    def get_album(self, pk):
        user = Album.objects.get(pk=pk)
        if user:
            return user
        else:
            return None
    def patch(self, request, pk):
        user = self.get_album(pk)
        if user == None:
            return Response({
                "status": "fail",
                "message": "Album is not found"
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_date['updatedAt'] = datetime.now()
            serializer.save()
            return Response({
                "status": "success",
                "data": {
                    "album": serializer.data
                }
            }, status=status.HTTP_200_OK)
        return Response({
            "status": "fail",
            "message": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        album = self.get_album(self, pk)
        if album == None:
            return Response({
                "status": "fail",
                "message": "Album is not found."
            }, status=status.HTTP_404_NOT_FOUND)
        album.delete()
        return Response({
            "status": "success",
            "message": "Album deleted successfully."
        }, status=status.HTTP_204_NO_CONTENT)

class User(generics.GenericAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

    def get(self, request):
    #    Query from queryParameter
        # pagination
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        #search params
        search_param = request.GET.get("search")
        users = UserModel.objects.all()
        total_users = users.count()

        if search_param:
            users = users.filter(title__icontains=search_param)
        serializer = self.serializer_class(users[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_users,
            "page": page_num,
            "last_page": math.ceil(total_users / limit_num),
            "notes": serializer.data
        })
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": {"user": serializer.data}
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "status": "fail",
                "message": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    def get_user(self,pk):
        try:
            return UserModel.objects.get(pk=pk)
        except:
            return None
    def patch(self, request, pk):
        user = self.get_user(pk)
        if user == None:
            return Response({
                "status": "fail",
                "message": "User not found"
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({
                "status": "success",
                "data": {
                    "user": serializer.data
                }
            }, status=status.HTTP_200_OK)
        return Response({
            "status": "fail",
            "message": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        user = self.get_user(pk)
        if user == None:
            return Response({
                "status": "fail",
                "message": f"id is {pk}",
            }, status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )