from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView, ListAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User
from .serializers import RegisterSerializer, CustomLoginSerializer, UserSerializer, UserListForAdminSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        # Check if the username (name) is already taken
        name = request.data.get('name')
        if User.objects.filter(name=name).exists():
            return Response({'message': 'Name taken'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the email is already taken
        email = request.data.get('email')
        if User.objects.filter(email=email).exists():
            return Response({'message': 'Email taken'}, status=status.HTTP_400_BAD_REQUEST)

        response = super().create(request, *args, **kwargs)
        return Response({'message': 'Registeration succesfully done', "success": True})


class LoginView(TokenObtainPairView):
    serializer_class = CustomLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            raise AuthenticationFailed('Geçersiz e-posta veya şifre.')
        user = serializer.validated_data['user']
        access_token = str(AccessToken.for_user(user))

        return Response({'token': access_token})


class RetrieveUpdateUserView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        self.kwargs['pk'] = self.request.user.id
        queryset = User.objects.all()
        return queryset

    def update(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        return Response({'message': 'User updated succesfully', 'success': True})


class RetrieveUserByIdView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserListForAdminView(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserListForAdminSerializer


class UserDetailForAdminView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
