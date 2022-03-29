from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from django.http import HttpResponse
from .serializer import AboutSerializer, AlbumSerializer, AlbumDetailSerializer, StorySerializer, StoryDetailSerializer, VideoDetailSerializer, VideoSerializer
from .models import AboutModel, AlbumModel, StoryModel, VideoModel
from django.conf import settings


class AboutAPIView(generics.ListAPIView):
    serializer_class = AboutSerializer
    def get_queryset(self):
        qs = AboutModel.objects.all()
        return qs
    
    def get(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data='nothing found')


class AlbumAPIView(generics.ListAPIView):
    serializer_class = AlbumSerializer

    def get_queryset(self):
        qs = AlbumModel.objects.filter(published=True)
        return qs
    
    def get(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data='nothing found')


class AlbumDetailAPIView(generics.RetrieveAPIView):
    serializer_class = AlbumDetailSerializer

    def get_object(self):
        return self.kwargs.get('pk')
    
    def get_queryset(self):
        id = self.get_object()
        qs = AlbumModel.objects.filter(published=True).filter(id=id)
        return qs

    def get(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data='nothing found')


class StoryAPIView(generics.ListAPIView):
    serializer_class = StorySerializer

    def get_queryset(self):
        qs = StoryModel.objects.filter(published=True)
        return qs
    
    def get(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data='nothing found')


class StoryDetailAPIView(generics.RetrieveAPIView):
    serializer_class = StoryDetailSerializer

    def get_object(self):
        return self.kwargs.get('pk')
    
    def get_queryset(self):
        id = self.get_object()
        qs = StoryModel.objects.filter(published=True).filter(id=id)
        return qs

    def get(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data='nothing found')


class VideoAPIView(generics.ListAPIView):
    serializer_class = VideoSerializer

    def get_queryset(self):
        qs = VideoModel.objects.filter(published=True)
        return qs
    
    def get(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data='nothing found')


class VideoDetailAPIView(generics.RetrieveAPIView):
    serializer_class = VideoDetailSerializer

    def get_object(self):
        return self.kwargs.get('pk')

    def get_queryset(self):
        id = self.get_object()
        qs = VideoModel.objects.filter(published=True).filter(id=id)
        return qs
    
    def get(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data='nothing found')