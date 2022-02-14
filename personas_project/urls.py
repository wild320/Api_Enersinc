from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('api/', include('perfil_app_api.urls')),

]
