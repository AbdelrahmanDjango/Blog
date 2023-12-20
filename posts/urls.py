from django.urls import path, include
from .views import (PostList,
                    CommentList,
                    UserProfile,
                    UserPosts,
                    UserProfileDetail,
                    )
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers


router = routers.SimpleRouter()
router.register('posts', PostList)

second_router = routers.NestedSimpleRouter(router, 'posts', lookup='post')
second_router.register('comments', CommentList, basename='posts_comments')


routeruser = routers.SimpleRouter()
# routeruser.register('users', UserProfile, basename='user')
routeruser.register('userp', UserPosts, basename='user_posts')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(second_router.urls)),
    path('', include(routeruser.urls)),
    path('users/', UserProfile.as_view()),
    path('users/<int:pk>/', UserProfileDetail.as_view()),

    # path('', include(routeruserposts.urls)),
]