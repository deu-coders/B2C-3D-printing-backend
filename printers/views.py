from rest_framework import viewsets
from .serializers import PrinterSerializer, RequestmentSerializer
from .models import Printer, Requestment
from accounts.permissions import IsAuthor

# Create your views here.
class PrinterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Printer.objects.all()
    serializer_class = PrinterSerializer


class RequestmentViewSet(viewsets.ModelViewSet):
    queryset = Requestment.objects.all()
    serializer_class = RequestmentSerializer
    permission_classes = [IsAuthor]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
