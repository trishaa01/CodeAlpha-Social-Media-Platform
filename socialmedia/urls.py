from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
import os

def debug_view(request):
    cloud = os.environ.get('CLOUDINARY_CLOUD_NAME', 'NOT SET')
    key = os.environ.get('CLOUDINARY_API_KEY', 'NOT SET')
    storage = os.environ.get('DJANGO_SETTINGS_MODULE', 'NOT SET')
    return HttpResponse(f"CLOUD: {cloud} | KEY: {key} | SETTINGS: {storage}")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('debug-env/', debug_view),
    path('', include('users.urls')),
    path('', include('posts.urls')),
]