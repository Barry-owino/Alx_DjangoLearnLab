#from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from .models import Post, Comment
from accounts.models import CustomUser
from .serializers import PostSerializer, CommentSerializer
#from .permissions import IsOwnerOrReadOnly

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
        posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')  # Filter posts
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

