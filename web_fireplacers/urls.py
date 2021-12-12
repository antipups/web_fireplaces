from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include("fireplace_api.urls")),
    path('accounts/', include(('django.contrib.auth.urls', 'django.contrib.auth'), namespace='auth_system')),
]
