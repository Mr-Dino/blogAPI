import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from . import settings


urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns