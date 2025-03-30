from .serializers import ShareOwnershipSerializer, ShareOwnershipListSerializer
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView
from .models import ShareOwnership
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class ShareOwnershipCreateAPIView(CreateAPIView):
    queryset = ShareOwnership.objects.all()
    serializer_class = ShareOwnershipSerializer
    permission_classes = [IsAdminUser]


class ProjectShareOwnershipListAPIView(ListAPIView):
    serializer_class = ShareOwnershipListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        project_to_be_fetched = self.request.query_params.get('projectId')
        queryset = ShareOwnership.objects.filter(project_id=project_to_be_fetched)
        return queryset


class UserShareOwnershipListAPIView(ListAPIView):
    serializer_class = ShareOwnershipListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_to_be_fetched = self.request.query_params.get('userId')
        queryset = ShareOwnership.objects.filter(user_id=user_to_be_fetched)
        return queryset


class ShareOwnershipDestroyAPIView(DestroyAPIView):
    queryset = ShareOwnership.objects.all()
    serializer_class = ShareOwnershipSerializer
    permission_classes = [IsAdminUser]
