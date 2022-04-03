import email
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializer import UserLoginSerializer, UserSerializer
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

User = get_user_model()
def get_key_error_from_serializer_errors(serializer_error):
    return [key for key in serializer_error]

class UserRegisterAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if not serializer.is_valid():
                fields_error = get_key_error_from_serializer_errors(serializer.errors)
                return Response(status=status.HTTP_400_BAD_REQUEST, data=fields_error)
            password = request.data['password']
            password = make_password(password)
            email = request.data['email']
            first_name = request.data['first_name']
            last_name = request.data['last_name']
            User.objects.create(password=password, email=email, first_name=first_name, last_name=last_name,)
            return Response(status=status.HTTP_200_OK, data='User Created')
        except :
            return Response(status=status.HTTP_400_BAD_REQUEST, data='Failed')