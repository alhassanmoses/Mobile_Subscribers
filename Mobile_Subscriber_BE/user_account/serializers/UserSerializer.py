import logging
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from user_account.models.User import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'firstname',
            'othernames',
            'email',
            'password'
        ]

    extra_kwargs = {
        'password': {'write_only': True}
    }


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'firstname',
            'othernames',
            'email',
            'password',
            'token'
        ]
        read_only_fields = ['token', 'firstname', 'othernames']

    # def validate(self, attrs):
    #     logging.error(f"================= Got here 1")
    #     email = attrs.get('email', '')
    #     password = attrs.get('password', '')

    #     user = authenticate(email=email, password=password)
    #     logging.error(f"================= Got here 2")

    #     if not user:
    #         raise AuthenticationFailed('Invalid Credential. Try again')

    #     logging.error(f"================= Got here 3")

    #     return {
    #         'id': user.id,
    #         'firstname': user.firstname,
    #         'email': user.email,
    #         'othernames': user.othernames,
    #         'tokens': user.tokens
    #     }
