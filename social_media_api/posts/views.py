from rest_framework import viewsets, permissions, filters, status
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.models import CustomUser
from rest_framework.views import APIView
from django.contrib.contenttypes.models import ContentType
from notifications.models import Notification

class LikePost(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        user = request.user

        # Ensure a user can't like a post more than once
        if Like.objects.filter(user=user, post=post).exists():
            return Response({'detail': 'You already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a Like object
        Like.objects.create(user=user, post=post)

        # Create a notification for the user
        Notification.objects.create(
            recipient=post.author,  # Assuming 'author' is a field in Post model
            actor=user,
            verb=f'liked your post: {post.title}',
            content_type=ContentType.objects.get_for_model(Post),
            object_id=post.id,
        )

        return Response({'detail': 'Post liked successfully!'}, status=status.HTTP_201_CREATED)

class UnlikePost(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        user = request.user

        # Ensure the user has liked the post before unliking
        try:
            like = Like.objects.get(user=user, post=post)
            like.delete()

            # Delete the notification related to this action
            Notification.objects.filter(
                recipient=post.author, actor=user, verb=f'liked your post: {post.title}'
            ).delete()

            return Response({'detail': 'Post unliked successfully!'}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({'detail': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)
        
def perform_create(self, serializer):
    comment = serializer.save(author=self.request.user)
    # Trigger notification
    Notification.objects.create(
        recipient=comment.post.author,
        sender=self.request.user,
        post=comment.post,
        notification_type='comment',
        message=f'{self.request.user.username} commented on your post.',
    )


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
    

