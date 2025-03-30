from rest_framework import serializers
from .models import ShareOwnership
from projects.models import Project
from users.models import User


class ShareOwnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShareOwnership
        fields = "__all__"


class ShareOwnershipListSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name', read_only=True)
    share_value = serializers.DecimalField(max_digits=10, decimal_places=2, source="project.shareValue", read_only=True)
    project_title = serializers.CharField(source='project.projectTitle', read_only=True)

    class Meta:
        model = ShareOwnership
        fields = ("id", "user", "user_name", "project", "project_title", "shares", "share_value")
