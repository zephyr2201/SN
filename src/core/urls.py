from django.contrib import admin
from django.urls import re_path
from django.urls import include, path
from social_network.urls import user_patterns, post_patterns
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="SN API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

api_patterns = [
    path('user/', include(user_patterns)),
    path('post/', include(post_patterns)),
]

urlpatterns = [
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/', include(api_patterns))
]
