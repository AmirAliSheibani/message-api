from django.urls import path
from .views import MessageAPI

urlpatterns = [
    path('chat/', MessageAPI.as_view(), name='message-API'),
]
