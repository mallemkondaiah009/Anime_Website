from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site
    path('', include('home.urls')),  # Home app routes for the root path
    path('accounts/', include('accounts.urls')),  # Accounts app with a unique prefix
]
