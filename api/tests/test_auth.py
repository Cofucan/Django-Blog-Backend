import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from api.models import Post, Comment


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
