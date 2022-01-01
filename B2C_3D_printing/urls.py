from django.urls import re_path, path, include
from django.contrib import admin
from django.views.generic import RedirectView, TemplateView

# https://github.com/iMerica/dj-rest-auth/blob/master/demo/demo/urls.py
urlpatterns = [
    re_path(r'^auth/', include('dj_rest_auth.urls')), #로그인, 로그아웃, 비밀번호 재설정 및 비밀번호 변경과 같은 기본 인증 기능이 있습니다.
    re_path(r'^registration/', include('dj_rest_auth.registration.urls')), #등록 및 소셜 미디어 인증과 관련된 논리가 있습니다.
    
    # 이메일 관련 필요
    # https://hwan-hobby.tistory.com/91
    re_path(r'^account/', include('allauth.urls')),
    re_path(r'^admin/', admin.site.urls),
]