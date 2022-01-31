from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username', 'number', 'avatar']
        read_only_fields = ['username', 'number', 'avatar']


class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'avatar', 'number', 'password']
        extra_kwargs = {
            'password':{'write_only': True},
        }

    def validate_password(self, value):
        if len(value) < 8:
            raise ValueError('Password is too short')
        elif len(value) > 20:
            raise ValidationError('Password is too long')
        else:
            return value
