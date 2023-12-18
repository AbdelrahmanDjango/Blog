import json
from rest_framework.views import APIView
from .serializers import (UserSerializer,
                          ProfileSerializer,
                          FollowUnFollowSerializer,
                          FollowUnFollowSerializerSorted,
                          )
from .models import User, Profile, FollowUnFollow
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from rest_framework import status, generics, viewsets
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.http import Http404


# class Register(APIView):
#     permission_classes = [AllowAny]
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
# When I make save(); the data that I put in Postman will be added in admin panel, not just test.
#         serializer.save()
#         return Response(serializer.data)

# class LoginView(APIView):
#     permission_classes = [AllowAny]
#     def post(self, request):
#         email = request.data['email']
#         password = request.data['password']
#         user = User.objects.filter(email=email).first()
#
#         if user is None:
#             raise AuthenticationFailed('Failed data.')
#         if not user.check_password(password):
#             raise AuthenticationFailed('Password is wrong.')
#         payload = {
#             'id' : user.id,
#             'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=120),
#             'iat' : datetime.datetime.utcnow()
#         }
#         # payload_str = json.dump(payload)
#         token = jwt.encode(payload, 'secret', algorithm='HS256')
#
#         response = Response()
#         response.set_cookie(key='jwt', value=token, httponly=True)
#         response.data = {
#             # 1/2
#             'jwt' : token
#         }
#         return response
# # Get user's cookies.
# class UserView(APIView):
#     permission_classes = [AllowAny]
#     def get(self, request):
#         # 2/2
#         token = request.COOKIES.get('jwt')
#         if not token :
#             raise AuthenticationFailed('Token failed.')
#
#         try :
#             payload = jwt.decode(token, 'secret', algorithms=['HS256'])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Jwt failed.')
#         user = User.objects.filter(id = payload['id']).first()
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
# class LogoutView(APIView):
#     permission_classes = [AllowAny]
#     def post(self, request):
#         response = Response()
#         response.delete_cookie('jwt')
#         response.data = {
#             'message' : 'success',
#         }
#         return response
# return Response with message in dictionary. Don't return user becauser it asked JSON.
#         return Response({
#             'message':'success'
#         })

# Fetch all profiles and create new profile
class ProfileDetails(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    # def get(self, request):
    #     profile = Profile.objects.all()
    #     serializer = ProfileSerializer(profile, many=True)
    #     return Response(serializer.data)
    # def post(self, request):
    #     serializer = ProfileSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
# Fetch one profile
class ViewsProfile(APIView):
    def get(self, request, pk):
        profile = Profile.objects.get(id=pk)
        # bio = profile.bio.replace('\r\n', '\n').replace('\n\n', '\n').replace('\r\r', '\n') if profile.bio else None
        # profile.bio = bio
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

# Follow profile
class FollowProfile(generics.CreateAPIView):

    serializer_class = FollowUnFollowSerializer

    def perform_create(self, serializer):
        user_pk = self.kwargs.get('user_pk')
        profile_pk = self.kwargs.get('profile_pk')
        user = get_object_or_404(User, pk=user_pk)
        profile = get_object_or_404(Profile, pk=profile_pk)
        serializer.save(user_id=user, profile=profile, follow_status='follow')


# Unfollow profile
class UnFollowProfile(generics.RetrieveDestroyAPIView):
    serializer_class = FollowUnFollowSerializer

    def get_object(self):
        user_pk = self.kwargs.get('user_pk')
        profile_pk = self.kwargs.get('profile_pk')
        follow_instance = FollowUnFollow.objects.filter(user_id=user_pk, profile=profile_pk, follow_status='follow')
        if not follow_instance.exists():
            raise Http404('FollowUnFollow not found.')

        return follow_instance.first()

    def destroy(self, request, *args, **kwargs):
        follow_instance = self.get_object()
        follow_instance.delete()
        return Response({'message':'Successfully unfollowed'}, status=status.HTTP_200_OK)

# Find all followes of some profile
class ViewFollowers(APIView):
    def get(self, request, pk):
        fetch_profile = FollowUnFollow.objects.filter(profile=pk, follow_status='follow')
        if fetch_profile:
            serializer = FollowUnFollowSerializerSorted(fetch_profile, many=True)
            return Response(serializer.data)
        else:
            return Response('Don\'t have followers.')
# Find all following of some user.
class ViewFollowings(APIView):
    def get(self, request, pk):
        fetch_user = User.objects.get(id=pk)
        following_user = fetch_user.followunfollow_set.all()
        if following_user:
            serializer = FollowUnFollowSerializerSorted(following_user, many=True)
            return Response(serializer.data)
        else:
            return Response('Don\t have following.')
