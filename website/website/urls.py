from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('students/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('', include('blog.urls'))
]
