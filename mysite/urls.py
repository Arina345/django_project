from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('docs.urls')),
    path('admin/', admin.site.urls),
]