from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()

router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
<<<<<<< HEAD
router.register('profile', views.UserProfileViewSet)
=======
>>>>>>> b4ff86bade7bde95aaab8c6bf892548e748d93a8

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]
