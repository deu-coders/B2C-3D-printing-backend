from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from dj_rest_auth.serializers import UserDetailsSerializer

from .models import CustomUser

# https://velog.io/@ready2start/DRF-djrestauth%EB%A1%9C-%EC%BB%A4%EC%8A%A4%ED%85%80-%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0
class CustomRegisterSerializer(RegisterSerializer):
    # 기본 설정 필드: username, password, email
    # 추가 설정 필드: profile_image
    # profile_image = serializers.ImageField(use_url=True)

    # def get_cleaned_data(self):
    #     data = super().get_cleaned_data()
    #     data['profile_image'] = self.validated_data.get('profile_image', '')

    #     return data

    username = None
    name = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=300)
    address = serializers.CharField(max_length=300)


class CustomLoginSerializer(LoginSerializer):
    # 기본 설정 필드: username, password, email
    username = None

# https://krakensystems.co/blog/2020/custom-users-using-django-rest-framework
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'name', 'phone', 'address')
