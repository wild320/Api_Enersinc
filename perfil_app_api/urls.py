from django.urls import path,include
from rest_framework.routers import DefaultRouter
from perfil_app_api import views

router = DefaultRouter()
# router.register('hello-viewset', views.HelloViewSet,basename='hello-viewset')
router.register('perfil',views.UserProfileViewSet)

urlpatterns = [
    # path('hello-view/', views.PersonaApiView.as_view()),
    path('',include(router.urls))


]