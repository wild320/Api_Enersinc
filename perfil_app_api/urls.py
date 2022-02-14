from django.urls import path,include
from rest_framework.routers import DefaultRouter
from perfil_app_api import views

router = DefaultRouter()

router.register('personas',views.UserProfileViewSet)

urlpatterns = [
    
    path('',include(router.urls))

]