Created Custom User Model 

Extended Django's AbstractUser with:
Bio field (text)
Profile picture uploads
Followers system (M2M relationship)
Token-based authentication system
Secure password handling

API Endpoints
User Registration (POST /api/auth/register/)
Token-based Login (POST /api/auth/login/)
User Profile Management (GET/PATCH /api/auth/profile/)

Key Components
Custom serializers for user data handling
Token-authenticated views for profile management
Initial database migrations
Media file configuration for profile pictures

Technologies Used
Django 4.x
Django REST Framework
Token Authentication
SQLite (default database)


Authentication System
REST Framework Token Authentication
Token generation/return on registration/login
Protected endpoints requiring Authorization headers

Testing Performed
User registration flow verification
Token generation/validation tests
Profile retrieval/update functionality
Media upload capability check
