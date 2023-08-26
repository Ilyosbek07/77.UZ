from django.contrib.auth.hashers import make_password
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.contrib.auth.models import UserManager as AbastractUserManager
from django.utils.translation import gettext_lazy as _

phone_regex_validator = RegexValidator(
    regex=r"^\+?1?\d{9,12}$",
    message=_("Номер телефона необходимо вводить в формате: «+99891234567». Допускается до 13 цифр."),
)


class UserManager(AbastractUserManager):
    def _create_user(self, phone_number, password, **extra_fields):
        """
        Create and save a user with the given phone_number and password.
        """
        if not phone_number:
            raise ValueError("The given phone number must be set")

        user = self.model(phone_number=phone_number, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(phone_number, password, **extra_fields)

    def create_user(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone_number, password, **extra_fields)


class User(AbstractUser, BaseModel):
    fullname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    phone = models.CharField(max_length=125)
    photo = models.FileField(upload_to='user/images')
    email = models.EmailField(unique=True)
    location = models.URLField()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
