from django.contrib.auth.models import AbstractUser, Group, Permission, BaseUserManager
from django.conf import settings
from django.db import models

# Create your models here.

#customeUserManager with superuser
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)

#customUser model with date_of_birth and profile_photo
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    groups = models.ManyToManyField(
            'auth.Group',
            verbose_name='groups',
            blank=True,
            help_text='The groups this user belongs to.',
            related_name="customer_groups",
            related_query_name="user",
            )

    user_permissions = models.ManyToManyField(
           'auth.Permission',
            verbose_name='user permissions',
            blank=True,
            help_text='Specific permissions for this user.',
            related_name="customer_permissions",
            related_query_name="user",
           )

    def __str__(self):
        return self.username


class Book(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
                ("can_view", "Can view book"),
                ("can_create", "Can create book"),
                ("can_edit", "Can edit book"),
                ("can_delete", "Can delete book"),
        ]
    
    def __art__(self):
        return self.title
