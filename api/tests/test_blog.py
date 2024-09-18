import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from api.models import Post, Comment


@pytest.mark.django_db
def test_create_post(test_user):
    client = APIClient()
    client.force_authenticate(user=test_user)
    url = reverse('post-list')
    data = {
        'title': 'Test Post',
        'content': 'This is a test post',
        # 'author': test_user.id
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 201
    assert response.data['title'] == 'Test Post'
    assert response.data['content'] == 'This is a test post'
    assert response.data['author'] == test_user.username


@pytest.mark.django_db
def test_create_comment(test_user, test_post):
    client = APIClient()
    client.force_authenticate(user=test_user)
    url = reverse('comment-list')
    data = {
        'post': test_post.id,
        'content': 'This is a test comment',
        'author': test_user.id
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 201
    assert response.data['content'] == 'This is a test comment'
    assert response.data['author'] == test_user.username
    assert response.data['post'] == test_post.id
