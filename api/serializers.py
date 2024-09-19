from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post, Comment


# User = settings.AUTH_USER_MODEL
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, allow_blank=True)  # Make username optional
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data: dict):
        user = User(
            email=validated_data['email'],
            username=validated_data.get('username', None),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')
    post = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = Comment
        fields = '__all__'
