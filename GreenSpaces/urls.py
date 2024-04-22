from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gisapp.urls')),  # Corrected URL pattern for the root path
]
