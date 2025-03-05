from django.contrib.auth.decorators import user_passes_test

def role_required(*roles):
    def check_role(user):
        return (
            user.is_authenticated and
            hasattr(user, 'userprofile') and
            user.userprofile.role in roles
        )
    return user_passes_test(check_role, login_url='/login/')
