from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude =['user_permissions', 'groups', 'last_login', 'is_superuser', 'is_active', 'is_staff', 'is_admin', 'date_joined']


class UserLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude =['user_permissions', 'groups', 'last_login', 'is_superuser', 'is_active', 'is_staff', 'is_admin', 'first_name', 'last_name', 'email']
    
    def validate_password(self, value: str) -> str:
        """
         value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)