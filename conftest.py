import pytest
from api.models import Post, Comment
from django.contrib.auth import get_user_model


User = get_user_model()


# Test superuser
@pytest.fixture
def superuser():
    return User.objects.create_superuser('admin', 'testadmin@brainiac.com', '12345678')


@pytest.fixture
def test_user():
    user = User.objects.create_user('alphaone', 'alphaonea@brainiac.com', '12345678')
    return user


@pytest.fixture
def test_post(test_user):
    post = Post.objects.create(title='Test Post', content='This is a test post', author=test_user)
    return post


@pytest.fixture
def test_comment(test_user, test_post):
    comment = Comment.objects.create(post=test_post, content='This is a test comment', author=test_user)
    return comment
