from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpRequest


class LoginService:
    def __init__(self, request: HttpRequest):
        self.request = request

    def login_user(self, username: str, password: str) -> User:
        user = self._authenticate_user(username, password)
        login(self.request, user)
        return user

    def _authenticate_user(self, username: str, password: str) -> User:
        user = authenticate(self.request, username=username, password=password)
        if not user:
            raise Exception("There's no such a user")
        return user
