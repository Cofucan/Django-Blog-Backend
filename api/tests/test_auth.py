import pytest
from django.urls import reverse
from rest_framework.test import APIClient


# Test that user can signup with only email and password
@pytest.mark.django_db
def test_user_signup():
    client = APIClient()
    url = reverse('user-registration')
    data = {
        'email': 'testuser@blog.com',
        'password': '12345678'
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 201
    assert response.data['email'] == 'testuser@blog.com'
    assert response.data['username'] is None
    assert 'password' not in response.data


# Test that user cannot signup with only username and password
@pytest.mark.django_db
def test_user_signup_username():
    client = APIClient()
    url = reverse('user-registration')
    data = {
        'username': 'testuser',
        'password': '12345678'
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 400


# Test successful user login
@pytest.mark.django_db
def test_user_login(test_user):
    client = APIClient()
    url = reverse('token_obtain_pair')
    data = {
        'email': test_user.email,
        'password': '12345678'
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 200


# Test failed user login with wrong password
@pytest.mark.django_db
def test_user_login_wrong_password(test_user):
    client = APIClient()
    url = reverse('token_obtain_pair')
    data = {
        'email': test_user.email,
        'password': '87654321'
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 401
