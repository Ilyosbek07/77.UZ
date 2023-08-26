from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'fullname',
            'email',
            'phone_number',
            'profile_photo',
            'address'
        )


class RegisterUserSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField()
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "full_name",
            "project_name",
            "category_id",
            'phone_number',
            'address',
            "password",
            "token",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "token": {"read_only": True},
        }

    def get_token(self, user):
        tokens = RefreshToken.for_user(user)
        data = {"refresh": str(tokens), "access": str(tokens.access_token)}
        return data

    def create(self, validated_data):
        try:
            user = User.objects.create_user(**validated_data)
        except Exception as e:
            raise ValidationError(str(e))
        return user
