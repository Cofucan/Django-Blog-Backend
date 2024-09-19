from rest_framework import viewsets, permissions, serializers
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post, Comment
from .serializers import UserSerializer, PostSerializer, CommentSerializer
from .permission import IsAuthorOrReadOnly


class UserRegistrationView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        # Get the post ID from the request data
        post_id = self.request.data.get('post')

        # Validate that the post ID is an integer and exists
        try:
            post = Post.objects.get(pk=post_id)
        except (ValueError, Post.DoesNotExist):
            raise serializers.ValidationError("Invalid or non-existent post ID.")

        # Save the comment with the author and post
        serializer.save(author=self.request.user, post=post)
