from django.urls import path
from .views import UserRegisterAPIView


urlpatterns=[
    path('register/', UserRegisterAPIView.as_view()),
]