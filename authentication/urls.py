from django.contrib import admin
from django.urls import path, include
from auth_site.views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('auth_site.urls')),
    path('accounts/', include('allauth.urls')),
    path('logout/', include('django.contrib.auth.urls')),
]
