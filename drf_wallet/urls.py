"""
drf_wallet URL Configuration
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # url for admin-page
    path('auth/', include('djoser.urls')),  # url for djoser auth
    path('auth/', include('djoser.urls.jwt')),  # url for djoser jwt-auth
    path('API/v1/', include('wallet.urls')),  # url for drf_wallet app
]
