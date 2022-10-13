from django.db import router
from django.urls import path,include

from rest_framework.routers import DefaultRouter

from profile_api import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSets, basename='hello-viewset')
router.register('profile',views.UserProfileViewSet)
router.register('feed',views.UserProfileFeedViewSet)

urlpatterns =[
    path('hello-view/',views.HelloApiView.as_view()),
    path('login',views.UserLoginView.as_view()),
    path('',include(router.urls))
]