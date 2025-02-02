from django.contrib import admin
from django.urls import path
from django.urls import include     # include app urls routes also

urlpatterns = [
    path('',include("apps.home.urls")),   # homepage path
    path('admin/', admin.site.urls),    # admin path
]
