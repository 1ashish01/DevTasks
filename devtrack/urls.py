from django.contrib import admin
from django.urls import path, include
from issues.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('issues.urls')),
    path('', home, name='home'),
]