from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    groups = models.ManyToManyField( "auth.Group", related_name="customuser_set", blank=True )
    user_permissions = models.ManyToManyField( "auth.Permission", related_name="customuser_permissions_set", blank=True )
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)


    def __str__(self):
        return self.username
