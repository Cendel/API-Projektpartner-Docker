from django.urls import path
from .views import RegisterView, LoginView, RetrieveUpdateUserView, RetrieveUserByIdView, UserListForAdminView, \
    UserDetailForAdminView

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('user/', RetrieveUpdateUserView.as_view(), name="user_detail"),
    path('user/<int:pk>/', RetrieveUserByIdView.as_view(), name="user_profile"),
    path('auth/users/', UserListForAdminView.as_view(), name="user_auth_list"),
    path('user/<int:pk>/', UserDetailForAdminView.as_view(), name='user_auth_detail'),
    path('user/<int:pk>/update/', UserDetailForAdminView.as_view(), name='user_auth_update'),
    path('user/<int:pk>/delete/', UserDetailForAdminView.as_view(), name='user_auth_delete'),

]
