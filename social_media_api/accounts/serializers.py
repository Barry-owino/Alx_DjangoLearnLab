from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    # Define fields with CharField
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # Use create_user() to ensure proper user creation
        user = User.objects.create_user(**validated_data)

        token = Token.objects.create(user=user)

        return user



