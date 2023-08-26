from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.users.models import User
from apps.users.serializers import RegisterUserSerializer, UserSerializer


class UserProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = [IsAuthenticated]
