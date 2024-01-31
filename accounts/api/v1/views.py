from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import exceptions
from shop.permissions import IsAdminOrReadOnly
from .serializer import UserSerializer, LoginSerializer
from django.contrib.auth.models import User


class UserViewSet(
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrReadOnly]
    authentication_classes = [TokenAuthentication]


class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = serializer.validated_data.get('password')
        username = serializer.validated_data.get('username')
        user = User.objects.filter(username=username).first()
        if not user:
            raise exceptions.ValidationError('User doesn\'t exist')
        if not user.check_password(password):
            raise exceptions.ValidationError('Incorrect password')
        token, _ = Token.objects.update_or_create(user=user, defaults={"key": Token.generate_key()})
        return Response({"token": str(token)})
