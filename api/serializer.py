from rest_framework import serializers
from .models import AboutModel, AlbumModel, StoryModel, ImageModel, VideoModel


class ImageDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageModel
        fields = ['image_describe', 'image']


class AboutSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(source='self_image.image', read_only=True)
    class Meta:
        model = AboutModel
        fields = ['first_name', 'last_name', 'image', 'age', 'birthday', 'degree', 'trophy', 'self_describe']


class AlbumSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(source='album_thumbnail.image', read_only=True)
    class Meta:
        model = AlbumModel
        fields = ['id', 'name', 'thumbnail']


class AlbumDetailSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField(source='get_images')
    thumbnail = serializers.ImageField(source='album_thumbnail.image', read_only=True)
    class Meta:
        model = AlbumModel
        fields = ['name', 'album_describe', 'thumbnail', 'images']

    def get_images(self, obj):
        qs = obj.album_image.all()
        serializer = ImageDetailSerializer(qs, many=True)
        return serializer.data


class StorySerializer(serializers.ModelSerializer):
    image = serializers.ImageField(source='story_image.image', read_only=True)
    class Meta:
        model = StoryModel
        fields = ['id', 'name', 'image']


class StoryDetailSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(source='story_image.image', read_only=True)
    class Meta:
        model = StoryModel
        fields = ['name', 'image', 'story']


class VideoSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(source='video_thumbnail.image', read_only=True)
    class Meta:
        model = VideoModel
        fields = ['id', 'name', 'thumbnail']


class VideoDetailSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(source='video_thumbnail.image', read_only=True)
    class Meta:
        model = VideoModel
        fields = ['name', 'thumbnail', 'video_describe', 'video', 'story']