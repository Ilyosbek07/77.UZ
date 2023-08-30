from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from apps.users.models import User
from apps.users.serializers import RegisterUserSerializer, UserSerializer
from rest_framework.permissions import IsAdminUser
from drf_yasg.utils import swagger_auto_schema


class UserProfileView(APIView):
    def get(self, request: Request, *args, **kwargs) -> Response:
        user = self.request.user
        if user.is_authenticated:
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response({"message": "User is not authenticated"}, status=400)


# class RegistrationView(generics.CreateAPIView):
#     queryset = None
#     serializer_class = RegisterUserSerializer
#     permission_classes = [IsAuthenticated]


class RegistrationView(APIView):
    permission_classes = (IsAdminUser,)
    serializer_class = RegisterUserSerializer

    @swagger_auto_schema(request_body=RegisterUserSerializer)
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


# class Login(TokenObtainPairView):
#     def post(self, request: Request, *args, **kwargs) -> Response:
#         response = super().post(request, args, kwargs)
#         return response
