from django.urls import path
from .views import ShareOwnershipCreateAPIView, ShareOwnershipDestroyAPIView, ProjectShareOwnershipListAPIView, \
    UserShareOwnershipListAPIView

urlpatterns = [
    # Diğer URL şablonları burada
    path('create/', ShareOwnershipCreateAPIView.as_view(), name='share_ownership_create'),
    path('list/', ProjectShareOwnershipListAPIView.as_view(), name='share_ownership_list'),
    path('list/user/', UserShareOwnershipListAPIView.as_view(), name='share_ownership_list'),
    path('delete/<pk>/', ShareOwnershipDestroyAPIView.as_view(), name='share_ownership_create'),
]
