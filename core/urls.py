from django.urls import path, include
from .views import *
urlpatterns = [
    path('', index, name='homepage'),
    path('webrtc', webrtc, name='webrtc'),
]
