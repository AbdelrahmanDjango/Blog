from rest_framework import serializers
# from django.conf import settings
from .models import Post, Comment
from users.models import User
from rest_framework_recursive.fields import RecursiveField
class CommentSerializer(serializers.ModelSerializer):
    # author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    author = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ('author', 'body', 'created_at', 'parent')
        extra_kwargs = {
            'post' : {'write_only' : True,'required': False},
            'parent' : {'required': False},
        }
    def get_author(self, obj):
        return obj.author.username
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['author'] = user
        return super().create(validated_data)

class PostSerialzer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('author', 'title', 'body', 'created_at', 'comments', 'email')
        extra_kwargs = {
        'email': {'write_only': True}
        }
    def get_author(self, obj):
        return obj.author.username
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['author'] = user
        return super().create(validated_data)
        # author = validated_data.get('author', None)
        # if author is None:
        #     raise serializers.ValidationError('Author must be specified.')
        # return Post.objects.create(author=author, **validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'id', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }


class PostForUserSerializerPosts(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'body')

class UserSerializerPosts(serializers.ModelSerializer):
    userposts = PostForUserSerializerPosts(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('username', 'userposts')
        extra_kwargs = {
            'password': {'read_only': True},
            'username': {'read_only': True}
        }


