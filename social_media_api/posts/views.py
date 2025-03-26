from rest_framework import viewsets, permissions, generics
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only owners to edit or delete their posts and comments.
    """

    def has_object_permission(self, request, view, obj):
        # Read-only permissions (GET, HEAD, OPTIONS) are allowed for any request.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed for the author of the post or comment.
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing posts.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing comments.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        """
        Optionally filter comments by post_id if provided in the request.
        """
        post_id = self.request.query_params.get("post_id")
        if post_id:
            return Comment.objects.filter(post_id=post_id)
        return Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get_query(self):
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-create_at')
