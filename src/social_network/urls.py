from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from social_network.apis import (
    SignUpApi, ActivityApi,
    PostCreateApi, LikeApi, UnLikeApi, LikeAnaliticsApi
)


user_patterns = [
    path('signup/', SignUpApi.as_view(), name='sign_up'),
    path('activity/', ActivityApi.as_view(), name='user_activity'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

post_patterns = [
    path('', PostCreateApi.as_view(), name='create_post'),
    path('<int:post_id>/like/', LikeApi.as_view(), name='like_post'),
    path('<int:post_id>/unlike/', UnLikeApi.as_view(), name='unlike_post'),
    path('like/analitics/', LikeAnaliticsApi.as_view(), name='like analitics'),
]
