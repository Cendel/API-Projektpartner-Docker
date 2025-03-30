from rest_framework import serializers
from .models import User
from share_ownership.models import ShareOwnership
from projects.models import Project
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirmPassword = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("id", "name", "email", "password", "confirmPassword")

    def create(self, validated_data):
        user = User.objects.create_user(
            **validated_data)
        user.set_password(
            validated_data[
                "password"])
        user.save()
        return user


class CustomLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)
            if not user:
                raise serializers.ValidationError('Invalid email or password')
            attrs['user'] = user
            return attrs
        else:
            raise serializers.ValidationError('Both email and password are required')


class UserSerializer(serializers.ModelSerializer):
    is_superuser = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()
    email = serializers.ReadOnlyField()
    followed_projects = serializers.SerializerMethodField()
    participated_projects = serializers.SerializerMethodField()
    created_projects = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id', "email", 'name', 'job', 'location', 'about', 'phone', 'website', "is_superuser", "followed_projects",
            "participated_projects", "created_projects")

    def get_followed_projects(self, obj):
        user = User.objects.filter(id=obj.id).first()
        followed_projects_query = user.followed_projects.all()
        followed_projects = []
        for project in followed_projects_query:
            followed_projects.append(project.id)

        return followed_projects

    def get_participated_projects(self, obj):
        user = User.objects.filter(id=obj.id).first()
        participated_projects_query = ShareOwnership.objects.filter(user_id=user.id)
        participated_projects = []
        for project in participated_projects_query:
            participated_projects.append(project.project.id)

        return participated_projects

    def get_created_projects(self, obj):
        user = User.objects.filter(id=obj.id).first()
        created_projects_query = Project.objects.filter(createdBy=user.id)
        created_projects = []
        for project in created_projects_query:
            created_projects.append(project.id)

        return created_projects


class UserListForAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email')
