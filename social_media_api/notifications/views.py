from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Notification

class NotificationListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Retrieve notifications for the logged-in user"""
        return Notification.objects.filter(recipient=self.request.user).order_by('-created_at')

    def list(self, request, *args, **kwargs):
        """Custom response format"""
        queryset = self.get_queryset()
        notifications = [
            {
                "actor": notification.actor.username,
                "verb": notification.verb,
                "created_at": notification.created_at,
                "is_read": notification.is_read
            }
            for notification in queryset
        ]
        return Response(notifications)

