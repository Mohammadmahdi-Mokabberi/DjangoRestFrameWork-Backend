from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .serializer import ChangePasswordSerializer, UserSerializer

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


class ChangePasswordAPIView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    def get_object(self):
        return self.request.user
    
    def update(self, request, *args, **kwargs):
        try:
            user = self.get_object()
            serializer = self.get_serializer(data=request.data)
            if not serializer.is_valid():
                return Response(status=status.HTTP_400_BAD_REQUEST, data='Changing Failed')
            
            old_password = request.data['old_password']
            new_password = request.data['new_password']
            new_password2 = request.data['new_password2']
            if not new_password == new_password2:
                return Response(status=status.HTTP_400_BAD_REQUEST, data='new password are not same')
        
            if not user.check_password(old_password):
                return Response(status=status.HTTP_400_BAD_REQUEST, data='old password is not correct')
            
            user.set_password(new_password)
            user.save()
            return Response(status=status.HTTP_200_OK, data='Password Changed')
            
        except :
            return Response(status=status.HTTP_400_BAD_REQUEST, data='Failed')