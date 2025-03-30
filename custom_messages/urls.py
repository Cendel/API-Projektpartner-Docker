from django.urls import path
from .views import MessageCreateAPIView, MessageRetrieveDestroyAPIView, MessagesListAPIView

urlpatterns = [
    path('create/', MessageCreateAPIView.as_view(), name='message_create'),
    path('<pk>/', MessageRetrieveDestroyAPIView.as_view(), name='message_get_delete'),
    path('', MessagesListAPIView.as_view(), name='messages_list'),
]
