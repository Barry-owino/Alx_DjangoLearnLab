from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'date_of_birth', 'profile_photo', 'email', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active', 'date_of_birth']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'date_of_birth', 'profile_photo', 'is_active', 'is_staff'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)

# Register the CustomUser model with the custom admin interface
admin.site.register(CustomUser, CustomUserAdmin)

