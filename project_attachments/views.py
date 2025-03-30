from rest_framework.response import Response
from rest_framework import status
from .serializers import AttachmentSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView
from .models import Attachment
from projects.models import Project
from rest_framework.permissions import IsAuthenticated


class AttachmentCreateAPIView(CreateAPIView):
    serializer_class = AttachmentSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        project_id = request.data.get('project')

        if Project.objects.get(id=project_id).createdBy_id == user.id or user.is_superuser:
            return super().create(request, *args, **kwargs)


class AttachmentsByProjectIdListAPIView(ListAPIView):
    serializer_class = AttachmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        project_to_be_fetched = self.request.query_params.get('projectId')
        queryset = Attachment.objects.filter(project_id=project_to_be_fetched)
        return queryset


class AttachmentDestroyAPIView(DestroyAPIView):
    queryset = Attachment
    serializer_class = AttachmentSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if request.user.is_authenticated and (
                request.user.is_superuser or request.user.id == instance.project.createdBy_id):
            self.perform_destroy(instance)
            return Response({"message": "Attachment deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

        return Response({"error": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)
