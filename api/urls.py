from django.urls import path
from .views import AlbumAPIView, AlbumDetailAPIView, AboutAPIView, StoryAPIView, StoryDetailAPIView, VideoAPIView, VideoDetailAPIView

urlpatterns = [
    path('album', AlbumAPIView.as_view()),
    path('album/<int:pk>', AlbumDetailAPIView.as_view()),
    path('story', StoryAPIView.as_view()),
    path('story/<int:pk>', StoryDetailAPIView.as_view()),
    path('video', VideoAPIView.as_view()),
    path('video/<int:pk>', VideoDetailAPIView.as_view()),
    path('about',AboutAPIView.as_view()),
]