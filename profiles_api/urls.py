from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet , UserLoginApiView , ProfileFeedViewSet


router = DefaultRouter()
router.register('profiles' , ProfileViewSet)
router.register('feed' , ProfileFeedViewSet)


urlpatterns = [
	path('' , include(router.urls)),
	path('login/' , UserLoginApiView.as_view())

]