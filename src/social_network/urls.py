from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from social_network.apis import (
    SignUpApi, ActivityApi,
    PostCreateApi, LikeApi, UnLikeApi, LikeAnaliticsApi
)


urlpatterns = [
    path('post/', PostCreateApi.as_view(), name='create_post'),
    path('post/<int:post_id>/like/', LikeApi.as_view(), name='like_post'),
    path('post/<int:post_id>/unlike/', UnLikeApi.as_view(), name='unlike_post'),
    path('post/like/analitics/', LikeAnaliticsApi.as_view(), name='like analitics'),

    path('user/signup/', SignUpApi.as_view(), name='sign_up'),
    path('user/activity/', ActivityApi.as_view(), name='user_activity'),
    path('user/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
