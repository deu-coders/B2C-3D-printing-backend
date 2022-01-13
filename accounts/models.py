from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, AbstractBaseUser, Permission, Group
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager
from django.db.models.manager import EmptyManager

# Create your models here.
# User model 이메일,비밀번호,이름,휴대폰번호,주소
# class CustomUser(AbstractUser):
#     username = None
#     first_name = None
#     last_name = None
#     email = models.EmailField(_('email address'), unique=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = [] # 필수로 받고 싶은 필드들 넣기 원래 소스 코드엔 email필드가 들어간다.

#     # Extra fields
#     # https://gist.github.com/amartya-dev/dae4f3ba16fe5d6dda02493aba1565e4
#     # GENDER_CHOICE = (("Male", "Male"), ("Female", "Female"), ("Others", "Others"))
#     # gender = models.CharField(max_length=10, choices=GENDER_CHOICE)
#     # date_of_birth = models.DateField(blank=True, null=True)
#     name = models.CharField(blank=True, max_length=100)
#     phone = models.CharField(blank=True, max_length=300)
#     address =  models.CharField(blank=True, max_length=300)

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = None
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(max_length=254, unique=True, db_index=True, primary_key=True)

    is_staff = models.BooleanField(default=False)  # a admin user; non super-user
    is_superuser = models.BooleanField(default=False)  # a superuser
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # 필수로 받고 싶은 필드들 넣기 원래 소스 코드엔 email필드가 들어간다.

    name = models.CharField(blank=True, max_length=100)
    phone = models.CharField(blank=True, max_length=300)
    address = models.CharField(blank=True, max_length=300)

    objects = CustomUserManager()

    def __str__(self):
        return self.email

# https://linuxtut.com/en/b97b55623d88cc36b55e/
