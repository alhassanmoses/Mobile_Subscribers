from rest_framework import generics, permissions
from user_account.serializers.UserSerializer import RegisterSerializer, LoginSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status


class RegisterAPI(generics.CreateAPIView):
    """
    This is a public endpoint used to register accounts for new users

    Sample Response:
    {
        "email": "moses.wuniche@gmail.com",
        "firstname": "kwabena",
        "othernames": "asare",
    }
    """

    permission_classes = [permissions.AllowAny, ]
    serializer_class = RegisterSerializer


class LoginAPI(generics.GenericAPIView):
    """
    This endpoint provides a login credentials for registered users

    Sample Response:
{
    "id": 1,
    "firstname": null,
    "othernames": null,
    "email": "moses@gmail.com",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Im1vc2VzQGdtYWlsLmNvbSIsImV4cCI6MTY0ODQwODAzOH0.6A1g_rcjVynEYM4OlvJyIt0ips1-U6Pi7LWHeIcrcdM"
}
    """
    permission_classes = [permissions.AllowAny, ]
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = authenticate(username=email, password=password)

        if user:
            serializer = self.serializer_class(user)

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'message': "Invalid credentials, try again."}, status=status.HTTP_401_UNAUTHORIZED)
