from django.urls import path, include
from rest_framework import routers
from .views import PrinterViewSet, RequestmentViewSet


router = routers.DefaultRouter()
router.register('printers', PrinterViewSet, basename='printer')
router.register('requestments', RequestmentViewSet, basename='requestment')

urlpatterns = [
    path('', include(router.urls)),
]
