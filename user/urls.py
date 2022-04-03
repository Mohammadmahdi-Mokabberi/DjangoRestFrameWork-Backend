from django.urls import path
from .views import ChangePasswordAPIView, UserRegisterAPIView


urlpatterns=[
    path('register/', UserRegisterAPIView.as_view()),
    path('change-password/', ChangePasswordAPIView.as_view()),
]