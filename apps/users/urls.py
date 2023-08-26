from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from apps.users.views import RegistrationView, UserProfileView, Login

urlpatterns = [
    path("seller/registration/", RegistrationView.as_view(), name="user_register"),
    path(
        "login/",
        Login.as_view(),
        name="token_obtain_pair",
    ),
    path('me/', UserProfileView.as_view(), name='user_profile'),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
