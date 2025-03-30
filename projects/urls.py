from django.urls import path
from .views import ProjectCreateAPIView, ProjectDetailView, ProjectsListByStatusView, ProjectsListByAdminAdviceView, \
    ProjectDetailAuthView, UpdateProjectFollowerView, ProjectListForUserTablesView, UpdateProjectStatusAPIView, \
    UpdateAdminAdviceAPIView, ProjectListByIds

urlpatterns = [
    path('create/', ProjectCreateAPIView.as_view(), name='project_create'),
    path('list/status/', ProjectsListByStatusView.as_view(), name='list_by_status'),
    path('list/advice/', ProjectsListByAdminAdviceView.as_view(), name='list_by_advice'),
    path('listforusertables/', ProjectListForUserTablesView.as_view(), name='list_for_user_tables'),
    path('listprojectsbyids/', ProjectListByIds.as_view(), name='list_projects_by_ids'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('auth/<int:pk>/', ProjectDetailAuthView.as_view(), name='project_auth_detail'),
    path('follow/<int:pk>/', UpdateProjectFollowerView.as_view(), name='project_participant_join'),
    path('updatestatus/<int:pk>/', UpdateProjectStatusAPIView.as_view(), name='project_status_update'),
    path('updateadvice/<int:pk>/', UpdateAdminAdviceAPIView.as_view(), name='project_advice_update'),
]
