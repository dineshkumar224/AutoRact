from django.urls import path
from . import views

urlpatterns = [
    path('video_capture', views.video_capture, name='video_capture'),
   
]
