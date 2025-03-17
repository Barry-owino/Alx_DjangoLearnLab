from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Authentication URLs
    path('login/', LoginView.as_view(template_name='blog/loin.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),

    #Existing post URLs
    path('', views.post_list, name='post_list'),
]
