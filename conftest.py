import pytest
from django.contrib.auth.models import User
from api.models import Post


# Test superuser
@pytest.fixture
def superuser():
    return User.objects.create_superuser('admin', 'testadmin@brainiac.com', '12345678')


@pytest.fixture
def test_user():
    user = User.objects.create_user('alphaone', 'alphaonea@brainiac.com', '12345678')
    return user


@pytest.fixture
def test_post(user):
    post = Post.objects.create(title='Test Post', content='This is a test post', author=user)
    return post
