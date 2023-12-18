from django.db import models
from django.utils import timezone
from rest_framework.authtoken.models import Token
from django.conf import  settings
# from mptt.models import MPTTModel, TreeForeignKey

class Post(models.Model):
    author  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='userposts')
    title   = models.CharField(max_length=250)
    body    = models.TextField()
    email   = models.EmailField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)

    class Meta :
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

        indexes = [
            models.Index(fields=['-created_at'])
        ]
    def __str__(self):
        return f'Commented by {self.author} on {self.post}'

# class Followers(models.Model):
#     name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     follower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

