import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.test import RequestFactory
from django.contrib.auth import authenticate, login, logout

from accounts.views import logout_view


@pytest.mark.django_db
def test_login_view(client):
    # Create a test user
    username = 'test_user'
    password = 'test_password'
    User.objects.create_user(username=username, password=password)

    # Create a request object with POST data
    data = {'username': username, 'password': password}
    response = client.post(reverse('accounts:login'), data)

    # Check if the user is logged in and redirected
    assert response.status_code == 302
    assert response.url == reverse('shop:product_list')
    assert '_auth_user_id' in client.session


