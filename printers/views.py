from rest_framework import viewsets
from .serializers import PrinterSerializer, RequestmentSerializer
from .models import Printer, Requestment
from accounts.permissions import IsAuthor


class PrinterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Printer.objects.all()
    serializer_class = PrinterSerializer


class RequestmentViewSet(viewsets.ModelViewSet):
    queryset = Requestment.objects.all()
    serializer_class = RequestmentSerializer
    permission_classes = [IsAuthor]
    http_method_names = ['post', 'get', 'put', 'delete']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # https://tech.toktokhan.dev/2021/05/18/wide-django-knowledge/
    def get_queryset(self):
        user = self.request.user
        return Requestment.objects.filter(author=user)
