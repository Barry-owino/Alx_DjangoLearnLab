from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, permissions, generics, status
from .models import Post, Comment, Like
from notifications.models import Notification
from accounts.models import CustomUser
from .serializers import PostSerializer, CommentSerializer
from django.contrib.contenttypes.models import ContentType

# Create your views here.
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_created(self, serializer):
        serializer.save(author=self.request.user)


class UserFeedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        followed_users = user.following.all()  # Get users the current user follows
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')  # Filter posts
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        """Like a post and trigger a notification"""
        post = get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({"detail": "You already liked this post"}, status=status.HTTP_400_BAD_REQUEST)

        # Create a notification
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            target=post,
        )

        return Response({"detail": "Post liked"}, status=status.HTTP_201_CREATED)

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        """Unlike a post"""
        post = get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post)

        if not like.exists():
            return Response({"detail": "You haven't liked this post"}, status=status.HTTP_400_BAD_REQUEST)

        like.delete()
        return Response({"detail": "Post unliked"}, status=status.HTTP_204_NO_CONTENT)

