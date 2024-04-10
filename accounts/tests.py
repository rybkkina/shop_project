import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse
from django.test import RequestFactory
from django.contrib.auth import authenticate, login, logout
from django.test import Client

from accounts.services import LoginService
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


@pytest.mark.django_db
def test_register_view_post():
    client = Client()
    url = reverse('accounts:register')
    # Створюємо POST-запит з правильними даними форми
    data = {
        'username': 'testuser',
        'password1': 'testpassword123',
        'password2': 'testpassword123'
    }
    response = client.post(url, data)
    # Перевіряємо, чи користувач був успішно створений
    assert response.status_code == 302  # Очікуємо перенаправлення
    assert User.objects.filter(username='testuser').exists()  # Перевіряємо, чи існує користувач з цим ім'ям
    # Перевіряємо, чи користувач був автоматично увійшов
    user = authenticate(username='testuser', password='testpassword123')
    assert user is not None  # Перевіряємо, чи не є користувач None
    # Перевіряємо перенаправлення на сторінку списку продуктів
    assert response.url == reverse('shop:product_list')


@pytest.mark.django_db
def test_register_view_get():
    client = Client()
    url = reverse('accounts:register')
    response = client.get(url)  # Створюємо GET-запит
    assert response.status_code == 200  # Перевіряємо статус код, Очікуємо успішний запит
    # Перевіряємо, чи форма присутня у відповіді
    assert isinstance(response.context['form'], UserCreationForm)  # Перевіряємо, чи це екземпляр форми реєстрації


@pytest.fixture
def mock_request():
    return HttpRequest()


@pytest.fixture
def login_service(mock_request):
    return LoginService(mock_request)

'''
@pytest.mark.django_db
def test_login_user_successful(mocker, login_service, mock_request):
    # Create a mock user
    username = 'testuser'
    password = 'testpassword'
    user = User.objects.create_user(username=username, password=password)

    # Mock authenticate function
    authenticate_mock = mocker.patch('django.contrib.auth.authenticate')
    authenticate_mock.return_value = user

    # Mock login function
    login_mock = mocker.patch('django.contrib.auth.login')

    # Perform login
    logged_in_user = login_service.login_user(username, password)

    # Check if authenticate method was called with correct parameters
    authenticate_mock.assert_called_once_with(mock_request, username=username, password=password)

    # Check if login method was called with correct parameters
    login_mock.assert_called_once_with(mock_request, user)

    # Check if the returned user is the same as the created user
    assert logged_in_user == user'''


@pytest.mark.django_db
def test_login_user_invalid_credentials(mocker, login_service):
    # Mock authenticate function to return None
    mocker.patch('django.contrib.auth.authenticate', return_value=None)

    # Test with invalid credentials
    with pytest.raises(Exception) as e:
        login_service.login_user('nonexistentuser', 'invalidpassword')

    # Check if the correct exception is raised
    assert str(e.value) == "There's no such a user"
