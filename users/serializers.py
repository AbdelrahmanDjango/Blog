from rest_framework import serializers
from .models import User, Profile, FollowUnFollow


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'password' : {'write_only' : True}
        }


    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Profile
        fields = ('user', 'bio', 'job', 'address', 'image')

    def get_user(self, obj):
        return obj.user.username
class FollowUnFollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowUnFollow
        fields = '__all__'


class FollowUnFollowSerializerSorted(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    class Meta:
        model = FollowUnFollow
        fields = ('user', 'profile', 'follow_status')
    def get_profile(self, obj):
        return obj.profile.user.username

    def get_user(self, obj):
        return obj.user.username
