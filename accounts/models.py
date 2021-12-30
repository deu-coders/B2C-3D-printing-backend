from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager

# Create your models here.
# User model 이메일,비밀번호,이름,휴대폰번호,주소
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # 필수로 받고 싶은 필드들 넣기 원래 소스 코드엔 email필드가 들어간다.

    # Extra fields
    # https://gist.github.com/amartya-dev/dae4f3ba16fe5d6dda02493aba1565e4
    # GENDER_CHOICE = (("Male", "Male"), ("Female", "Female"), ("Others", "Others"))
    # gender = models.CharField(max_length=10, choices=GENDER_CHOICE)
    # date_of_birth = models.DateField(blank=True, null=True)
    name = models.CharField(blank=True, max_length=100)
    phone = models.CharField(blank=True, max_length=300)
    address =  models.CharField(blank=True, max_length=300)

    objects = CustomUserManager()

    def __str__(self):
        return self.email