from .models import Post, Comment
from rest_framework.views import APIView
from rest_framework import generics, permissions, status, viewsets
from .serializers import (
    PostSerialzer,
    CommentSerializer,
    UserSerializer,
    UserSerializerPosts,
    PostForUserSerializerPosts,)
from .permissions import IsAuthorOrReadOnly, IsAuthorOrReadOnlyUser
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from users.models import User
from rest_framework.decorators import action

class PostList(viewsets.ModelViewSet):
        permission_classes = (permissions.IsAuthenticated,)
        queryset = Post.objects.all()
        serializer_class = PostSerialzer
    # # Filter list posts for only auther (superuser).
    # def get_queryset(self):
    #     user = self.request.user
    #     return Post.objects.filter(author = user)


class CommentList(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_pk')
        post = get_object_or_404(Post, pk = post_id)
        serializer.save(author=self.request.user, post=post)


    def get_queryset(self):
        post_id = self.kwargs.get('post_pk')
        queryset = Comment.objects.filter(post_id=post_id)
        return queryset

# class ReplayList(viewsets.ModelViewSet):
#     permission_classes = [permissions.IsAuthenticated,]
#     serializer_class = ReplaySerializer
#     def perform_create(self, serializer):
#         comment_id = self.kwargs.get('comment_pk')
#         comment = get_object_or_404(Comment, pk = comment_id)
#         serializer.save(comment=comment, name = self.request.user)
#     def get_queryset(self):
#         comment_id = self.kwargs.get('comment_pk')
#         queryset = Replay.objects.filter(comment_id=comment_id)
#         return queryset

class UserProfile(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnlyUser,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserPosts(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = UserSerializerPosts
    def get_queryset(self):
        return User.objects.prefetch_related('userposts')

