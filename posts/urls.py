from django.urls import path, include
from .views import PostList, CommentList, UserProfile, UserPosts
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers


router = routers.SimpleRouter()
router.register('posts', PostList)

second_router = routers.NestedSimpleRouter(router, 'posts', lookup='post')
second_router.register('comments', CommentList, basename='posts_comments')

routeruser = DefaultRouter()
routeruser.register('users', UserProfile, basename='user')

routeruserposts = routers.SimpleRouter()
routeruserposts.register('userp', UserPosts, basename='user_posts')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(second_router.urls)),
    path('', include(routeruser.urls)),
    path('', include(routeruserposts.urls)),
    # path('userp/', UserPosts.as_view()),
    # path('userp/<int:user_pk>/', UserPosts.as_view()),
]
