from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', views.CustomObtainAuthToken.as_view(), name='login'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
]
