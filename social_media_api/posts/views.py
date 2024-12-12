from rest_framework import viewsets, permissions, filters, status
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Post
from rest_framework.permissions import IsAuthenticated
from accounts.models import CustomUser

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def user_feed(request):
    """Get the feed of posts from users the current user follows"""
    user = request.user
    following_users = user.following.all()  # Get the users the current user is following
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')  # Retrieve posts from followed users, ordered by creation date
    post_data = [{"id": post.id, "title": post.title, "content": post.content, "created_at": post.created_at} for post in posts]
    return Response(post_data, status=status.HTTP_200_OK)
    

