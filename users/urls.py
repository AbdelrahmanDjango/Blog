from django.urls import path, include
from .views import (
    # Register,
    #                 LoginView,
    #                 UserView,
    #                 LogoutView,
                    ProfileDetails,
                    ViewsProfile,
                    FollowProfile,
                    UnFollowProfile,
                    ViewFollowers,
                    ViewFollowings,)
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

urlpatterns = [
    # path('register', Register.as_view()),
    # path('login', LoginView.as_view()),
    # path('user', UserView.as_view()),
    # path('Logout', LogoutView.as_view()),
    path('profile_details/', ProfileDetails.as_view(), name='profile_list'),
    path('show_profile/<int:pk>/', ViewsProfile.as_view(), name='view_profile'),
    path('follow_profile/<int:user_pk>/<int:profile_pk>/', FollowProfile.as_view(), name='follow_profile'),
    path('unfollow_profile/<int:user_pk>/<int:profile_pk>/', UnFollowProfile.as_view(), name='unfollow_profile'),
    path('view_followers/<int:pk>/', ViewFollowers.as_view(), name='view_followers'),
    path('view_following/<int:pk>/', ViewFollowings.as_view(), name='view_following'),

]
