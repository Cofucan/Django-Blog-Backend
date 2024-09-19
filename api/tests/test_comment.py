import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

from api.models import Post, Comment


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
    assert response.data['author'] == test_user.email
    assert response.data['post'] == test_post.title


# Test that user cannot create a comment without authentication
@pytest.mark.django_db
def test_create_comment_unauthenticated(test_post):
    client = APIClient()
    url = reverse('comment-list')
    data = {
        'post': test_post.id,
        'content': 'This is a test comment',
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 401


# Test that user can update a comment
@pytest.mark.django_db
def test_update_comment(test_user, test_comment):
    client = APIClient()
    client.force_authenticate(user=test_user)
    url = reverse('comment-detail', args=[test_comment.id])
    data = {
        'content': 'This is an updated test comment',
    }
    response = client.put(url, data, format='json')
    assert response.status_code == 200
    assert response.data['content'] == 'This is an updated test comment'
    assert response.data['author'] == test_user.email
    assert response.data['post'] == test_comment.post.title


# Test that user cannot update a comment without authentication
@pytest.mark.django_db
def test_update_comment_unauthenticated(test_comment):
    client = APIClient()
    url = reverse('comment-detail', args=[test_comment.id])
    data = {
        'content': 'This is an updated test comment',
    }
    response = client.put(url, data, format='json')
    assert response.status_code == 401


# Test that user can delete a comment
@pytest.mark.django_db
def test_delete_comment(test_user, test_comment):
    client = APIClient()
    client.force_authenticate(user=test_user)
    url = reverse('comment-detail', args=[test_comment.id])
    response = client.delete(url)
    assert response.status_code == 204


# Test that user cannot delete a comment without authentication
@pytest.mark.django_db
def test_delete_comment_unauthenticated(test_comment):
    client = APIClient()
    url = reverse('comment-detail', args=[test_comment.id])
    response = client.delete(url)
    assert response.status_code == 401


# Test that user cannot delete a comment without being the author
@pytest.mark.django_db
def test_delete_comment_unauthorized(test_user, test_comment):
    client = APIClient()
    user = get_user_model().objects.create_user('testuser2', 'testuser2@blog.com', '12345678')
    client.force_authenticate(user=user)
    url = reverse('comment-detail', args=[test_comment.id])
    response = client.delete(url)
    assert response.status_code == 403


# Test that user cannot update a comment without being the author
@pytest.mark.django_db
def test_update_comment_unauthorized(test_user, test_comment):
    client = APIClient()
    user = get_user_model().objects.create_user('testuser2', 'testuser2@blog.com', '12345678')
    client.force_authenticate(user=user)
    url = reverse('comment-detail', args=[test_comment.id])
    data = {
        'content': 'This is an updated test comment',
    }
    response = client.put(url, data, format='json')
    assert response.status_code == 403
