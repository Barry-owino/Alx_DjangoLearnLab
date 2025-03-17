# Blog Authentication System

## Features
- User registration with email verification
- Login/logout functionality
- Profile management
- Password reset (TODO)
- Social auth integration (TODO)

## Testing Guide

1. Registration:
   - Visit /register
   - Submit valid credentials
   - Verify welcome email (in console)

2. Login:
   - Visit /login
   - Use registered credentials
   - Verify successful redirect

3. Profile Management:
   - Login first
   - Visit /profile
   - Update profile fields
   - Verify changes in admin

## Security Features
- CSRF protection on all forms
- Password hashing with PBKDF2
- Session-based authentication
- Login required decorator
