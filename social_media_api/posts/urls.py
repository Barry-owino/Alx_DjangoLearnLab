from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, UserFeedView, LikePostView, UnlikePostView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', UserFeedView.as_view(), name='user-feed'), #feed endpoint url

    path('<int:pk>/like/', LikePostView.as_view(), name='like-post'), #likepost endpoint url
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),  #unlikepost endpoint url
]
