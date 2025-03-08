from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings
from django.db import models

# Create your models here.

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
    
    def __art__(self):
        return self.title
