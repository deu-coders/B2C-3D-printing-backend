from rest_framework import viewsets
from .serializers import PrinterSerializer, RequestmentSerializer
from .models import Printer, Requestment
from accounts.permissions import IsAuthor

from django.shortcuts import render
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading

# Create your views here.


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


class VideoCamera(object):
    def __init__(self, video_id):
        self.video = cv2.VideoCapture(video_id)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@gzip.gzip_page
def VideoViewSet(request, video_id):
    try:
        cam = VideoCamera(video_id)
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        print("에러입니다...")
        pass
