from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'id', 'projectStatus', "adminAdvice", 'projectTitle', 'projectPlace', 'estimatedImplementationDate',
            'slogan', "about",
            "goal", "support", "shortDesc", "longDesc", "projectImage", "createdBy", "createdByName", "createdDate",
            "projectValue", "totalShares", "shareValue", "maxSharesPerPerson", "sharesTaken",
            "followerList")


class ProjectFollowerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['followerList']


class ProjectListForTablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'id', 'projectTitle', 'estimatedImplementationDate', "createdBy", "createdByName")


class ProjectStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["projectStatus"]


class ProjectAdminAdviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["adminAdvice"]
