from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('eDiary.urls')),
    path('reminder/', include('reminder.urls')),
]
