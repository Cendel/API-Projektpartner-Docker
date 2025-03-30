from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, \
    UpdateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .models import Project
from .serializers import ProjectSerializer, ProjectFollowerUpdateSerializer, ProjectListForTablesSerializer, \
    ProjectStatusSerializer, ProjectAdminAdviceSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.permissions import BasePermission


class IsProjectOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.createdBy_id == request.user.id or request.user.is_superuser


# create a project
class ProjectCreateAPIView(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        project = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)  # cre


# list projects by Status - either true or false
class ProjectsListByStatusView(ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        status_param = True if self.request.query_params.get(
            'projectStatus') == "true" else False
        queryset = Project.objects.filter(projectStatus=status_param)
        return queryset


# list projects by AdminAdvice - either true or false
class ProjectsListByAdminAdviceView(ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        status_param = True if self.request.query_params.get(
            'adminAdvice') == "true" else False
        queryset = Project.objects.filter(adminAdvice=status_param)
        return queryset


# list requested projects with all details
class ProjectListByIds(ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        project_ids = list(self.request.query_params.values())
        return Project.objects.filter(id__in=project_ids)


# list requested projects for Profiles
class ProjectListForUserTablesView(ListAPIView):
    serializer_class = ProjectListForTablesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        project_ids = list(self.request.query_params.values())
        return Project.objects.filter(projectStatus=True, id__in=project_ids)


# returns all details of a project
class ProjectDetailView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]


# returns/updates/deletes a project - accessible to admins and project owners
class ProjectDetailAuthView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsProjectOwner]


# follows/unfollows a project
class UpdateProjectFollowerView(UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectFollowerUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        user = self.request.user
        project = self.get_object()

        if project.followerList.filter(id=user.id).exists():
            project.followerList.remove(user)
        else:
            project.followerList.add(user)

        serializer.save(followerList=project.followerList.all())


# updates status of a project
class UpdateProjectStatusAPIView(UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectStatusSerializer
    permission_classes = [IsAdminUser]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()


# updates admin advice of a project
class UpdateAdminAdviceAPIView(UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectAdminAdviceSerializer
    permission_classes = [IsAdminUser]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()
