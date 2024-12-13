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
from django.shortcuts import get_object_or_404
from rest_framework import generics
from django.http import HttpResponse
from django.views import View
from django.http import JsonResponse

class LikePost(View):
    def post(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            post.likes += 1
            post.save()
            return JsonResponse({'message': 'Post liked successfully!', 'likes': post.likes})
        except Post.DoesNotExist:
            return JsonResponse({'error': 'Post not found'}, status=404)

class UnlikePost(View):
    def post(self, request, pk):
        # Add your functionality here to unlike the post
        return JsonResponse({"message": "Post unliked successfully!"})
    
def home(request):
    return HttpResponse("Welcome to the Social Media API!")

class LikePostView(generics.GenericAPIView):
    def post(self, request, pk):
        # Retrieve the post object using generics.get_object_or_404
        post = generics.get_object_or_404(Post, pk=pk)
        
        # Check if the user has already liked the post
        Like, created = Like.objects.get_or_create(user=request.user, post=post)
        
        if created:
            # Generate a notification for the post author
            Notification.objects.create(
                user=post.author,
                message=f'{request.user.username} liked your post: {post.title}',
                post=post
            )
            return Response({"message": "Post liked!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        
class UnlikePostView(generics.GenericAPIView):
    def delete(self, request, pk):
        # Retrieve the post object using generics.get_object_or_404
        post = generics.get_object_or_404(Post, pk=pk)
        
        # Try to retrieve and delete the like object if it exists
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()  # Delete the like
            return Response({"message": "Post unliked!"}, status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            return Response({"message": "You have not liked this post yet."}, status=status.HTTP_400_BAD_REQUEST)
        
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
    
@api_view(['POST'])
def like_post(request, pk):
    # Get the post object
    post = get_object_or_404(Post, pk=pk)
    
    # Check if the user has already liked the post
    Like, created = Like.objects.get_or_create(user=request.user, post=post)
    
    # If a new like is created, generate a notification
    if created:
        # You can customize the notification message as needed
        Notification.objects.create(
            user=post.author,
            message=f'{request.user.username} liked your post: {post.title}',
            post=post
        )
        return Response({"message": "Post liked!"}, status=status.HTTP_201_CREATED)
    else:
        return Response({"message": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def unlike_post(request, pk):
    # Get the post object
    post = get_object_or_404(Post, pk=pk)
    
    # Get the like object if it exists
    try:
        like = Like.objects.get(user=request.user, post=post)
        like.delete()  # Delete the like
        return Response({"message": "Post unliked!"}, status=status.HTTP_204_NO_CONTENT)
    except Like.DoesNotExist:
        return Response({"message": "You have not liked this post yet."}, status=status.HTTP_400_BAD_REQUEST)
