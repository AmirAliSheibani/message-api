from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Message
from .serializers import MessageSerializer, MessageCreateSerializer


class MessageAPI(GenericAPIView):
    queryset = Message.objects.all().order_by("created_at")
    serializer_class = MessageSerializer

    def get(self, request):
        messages = self.get_queryset()
        serializer = self.get_serializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MessageCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        message = serializer.save()

        return Response(
            {
                "status": "success",
                "message": "پیام دریافت شد",
                "data": MessageSerializer(message).data
            },
            status=status.HTTP_201_CREATED
        )
