"""core URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from rest_framework_jwt.views import (
    obtain_jwt_token, refresh_jwt_token, verify_jwt_token)

from .routers import router

urlpatterns = [

    url('^api-token-auth/', obtain_jwt_token),
    url('^api-token-refresh/', refresh_jwt_token),
    url('^api-token-verify/', verify_jwt_token),

    url(r'^admin/', admin.site.urls),
    url(r'^v1/', include(router.urls)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
