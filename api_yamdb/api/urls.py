from django.urls import include, path

from rest_framework.routers import DefaultRouter

from api.views import (CommentViewSet, ReviewViewSet, UserViewSet,
                       TitleViewSet, CategoryViewSet, GenreViewSet,
                       signup, get_token)

router_v1 = DefaultRouter()
router_v1.register('titles', TitleViewSet, basename='titles')
router_v1.register(
    r'categories',
    CategoryViewSet, basename='categories'
)
router_v1.register('genres', GenreViewSet, basename='genres')
router_v1.register(r'titles/(?P<title_id>\d+)/reviews',
                   ReviewViewSet, basename='reviews')
router_v1.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)'
                   r'/comments', CommentViewSet, basename='comments')
router_v1.register('users', UserViewSet, basename='users')

auth_path = [
    path('auth/signup/', signup),
    path('auth/token/', get_token)
]

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include(auth_path))
]
