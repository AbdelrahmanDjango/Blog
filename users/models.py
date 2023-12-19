from django.db import models
from django.contrib.auth.models import AbstractUser
from posts.models import Post
from django.urls import reverse

class User(AbstractUser):
    password = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    # username = models.CharField(max_length=250, unique=True)
    # REQUIRED_FIELDS = ['password']
    # USERNAME_FIELD = 'username'
    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.ImageField(upload_to='user_photos', blank=True)
    job = models.CharField(max_length=500,blank=True)
    address = models.CharField(max_length= 250, blank=True)

    def __str__(self):
        return self.user.username

class FollowUnFollow(models.Model):
    Follow = (
        ('follow', 'Follow'),
        ('unfollow', 'Unfollow')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    follow_status = models.CharField(max_length=100, choices=Follow)

    def __str__(self):
        return self.follow_status

