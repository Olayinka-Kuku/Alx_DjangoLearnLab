from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, LikePost
from . import views

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', views.user_feed, name='user_feed'),
    path('<int:pk>/like/', views.LikePost.as_view(), name='like_post'),
    path('<int:pk>/unlike/', views.UnlikePost.as_view(), name='unlike_post'),
]
