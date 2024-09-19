import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model


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
    assert response.data['author'] == test_user.email


# Test that user cannot create a post without authentication
@pytest.mark.django_db
def test_create_post_unauthenticated():
    client = APIClient()
    url = reverse('post-list')
    data = {
        'title': 'Test Post',
        'content': 'This is a test post',
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 401


# Test that user can update a post
@pytest.mark.django_db
def test_update_post(test_user, test_post):
    client = APIClient()
    client.force_authenticate(user=test_user)
    url = reverse('post-detail', args=[test_post.id])
    data = {
        'title': 'Updated Test Post',
        'content': 'This is an updated test post',
    }
    response = client.put(url, data, format='json')
    assert response.status_code == 200
    assert response.data['title'] == 'Updated Test Post'
    assert response.data['content'] == 'This is an updated test post'
    assert response.data['author'] == test_user.email


# Test that user cannot update a post without authentication
@pytest.mark.django_db
def test_update_post_unauthenticated(test_post):
    client = APIClient()
    url = reverse('post-detail', args=[test_post.id])
    data = {
        'title': 'Updated Test Post',
        'content': 'This is an updated test post',
    }
    response = client.put(url, data, format='json')
    assert response.status_code == 401


# Test that user can delete a post
@pytest.mark.django_db
def test_delete_post(test_user, test_post):
    client = APIClient()
    client.force_authenticate(user=test_user)
    url = reverse('post-detail', args=[test_post.id])
    response = client.delete(url)
    assert response.status_code == 204


# Test that user cannot delete a post without authentication
@pytest.mark.django_db
def test_delete_post_unauthenticated(test_post):
    client = APIClient()
    url = reverse('post-detail', args=[test_post.id])
    response = client.delete(url)
    assert response.status_code == 401


# Test that user cannot update another user's post
@pytest.mark.django_db
def test_update_post_unauthorized(test_user, test_post):
    client = APIClient()
    User = get_user_model()
    user = User.objects.create_user('betty', 'bettycool@blog.com', '12345678')
    client.force_authenticate(user=user)
    url = reverse('post-detail', args=[test_post.id])
    data = {
        'title': 'Updated Test Post',
        'content': 'This is an updated test post',
    }
    response = client.put(url, data, format='json')
    assert response.status_code == 403
