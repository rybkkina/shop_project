import pytest
from django.http import HttpRequest
from django.test import RequestFactory
from django.shortcuts import reverse, redirect
from django.contrib.auth.models import User
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from pytest_mock import mocker

from shop.models import Product
from cart.forms import CartAddProductForm
from cart.views import cart_add
from cart.cart import Cart


@pytest.fixture
def mock_request_factory():
    return RequestFactory()


@pytest.fixture
def mock_cart(mocker):
    return mocker.Mock(spec=Cart)


@pytest.fixture
def mock_product(mocker):
    return mocker.Mock(spec=Product)


@pytest.fixture
def mock_cart_add_product_form(mocker):
    return mocker.Mock(spec=CartAddProductForm)


@pytest.fixture
def mock_redirect(mocker):
    return mocker.patch('cart.views.redirect')


@pytest.mark.django_db
def test_cart_add_authenticated_user(mock_request_factory, mock_cart, mock_product, mock_cart_add_product_form,
                                     mock_redirect):
    # Create an authenticated user
    user = User.objects.create_user(username='testuser', password='password')

    # Create a request with an authenticated user
    request = mock_request_factory.post(reverse('cart:cart_add', kwargs={'product_id': 1}))
    request.user = user
    SessionMiddleware().process_request(request)

    # Mock the get_object_or_404 function
    mock_get_object_or_404 = mocker.patch('cart.views.get_object_or_404')
    mock_get_object_or_404.return_value = mock_product

    # Mock the CartAddProductForm
    mock_form = mock_cart_add_product_form.return_value
    mock_form.is_valid.return_value = True
    mock_form.cleaned_data = {'quantity': 1, 'override': True}

    # Call the view function
    response = cart_add(request, product_id=1)

    # Check if the cart.add method was called with the correct arguments
    mock_cart.add.assert_called_once_with(product=mock_product, quantity=1, override_quantity=True)

    # Check if redirect function was called with the correct argument
    assert response == mock_redirect.return_value
    mock_redirect.assert_called_once_with('cart:cart_detail')


@pytest.mark.django_db
def test_cart_add_unauthenticated_user(mock_request_factory, mock_redirect):
    # Create a request with an unauthenticated user
    request = mock_request_factory.post(reverse('cart:cart_add', kwargs={'product_id': 1}))

    # Call the view function
    response = cart_add(request, product_id=1)

    # Check if redirect function was called with the correct argument
    assert response == mock_redirect.return_value
