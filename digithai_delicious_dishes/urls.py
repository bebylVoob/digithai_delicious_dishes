from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from digithai_delicious_dishes import settings

urlpatterns = [
    path('cuisine/', include('cuisine.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]