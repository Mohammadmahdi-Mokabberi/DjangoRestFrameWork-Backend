from django.urls import path
from rest_framework_simplejwt import views
from .views import ChangePasswordAPIView, UserRegisterAPIView


urlpatterns=[
    path('register/', UserRegisterAPIView.as_view()),
    path('login/', views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('refresh/', views.TokenRefreshView.as_view(), name ='token_refresh'),
    path('change-password/', ChangePasswordAPIView.as_view()),
]