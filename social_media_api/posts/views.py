from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, permissions, generics, status
from .models import Post, Comment, Like
from notifications.models import Notification
from rest_framework.views import APIView
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

class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        user = request.user

        if Like.objects.filter(user=user, post=post).exists():
            return Response({"detail": "You have already liked this post."}, status=400)

        Like.objects.create(user=user, post=post)
        Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb="liked your post",
            target=post
        )

        return Response({"detail": "Post liked successfully."}, status=201)

class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        user = request.user

        like = Like.objects.filter(user=user, post=post)
        if not like.exists():
            return Response({"detail": "You have not liked this post."}, status=400)

        like.delete()
        return Response({"detail": "Post unliked successfully."}, status=200)


















