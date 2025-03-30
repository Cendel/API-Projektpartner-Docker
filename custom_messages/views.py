from .models import Message
from .serializers import MessageSerializer, MessageListSerializer
from rest_framework.generics import CreateAPIView, RetrieveDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class MessageCreateAPIView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]


class MessageRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAdminUser]


class MessagesListAPIView(ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageListSerializer
    permission_classes = [IsAdminUser]
