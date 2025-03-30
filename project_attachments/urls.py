from django.urls import path
from .views import AttachmentCreateAPIView, AttachmentsByProjectIdListAPIView, AttachmentDestroyAPIView

urlpatterns = [
    path('create/', AttachmentCreateAPIView.as_view(), name='attachment_create'),
    path('listbyproject/', AttachmentsByProjectIdListAPIView.as_view(), name='attachment_by_project'),
    path('delete/<int:pk>/', AttachmentDestroyAPIView.as_view(), name='attachment_by_project'),

]
