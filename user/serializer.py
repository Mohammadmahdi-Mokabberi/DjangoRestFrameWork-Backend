from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude =['user_permissions', 'groups', 'last_login', 'is_superuser', 'is_active', 'is_staff', 'is_admin', 'date_joined']


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()
    new_password2 = serializers.CharField()