from django.shortcuts import render
from .serializers import ProfileSerializer , ProfilefeedSerializer
from rest_framework import viewsets , filters
from .models import UserProfile , ProfileFeedItem
from .permissions import UpdateOwnProfile , UpdateOwnStatus
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly



class ProfileViewSet(viewsets.ModelViewSet):

	serializer_class = ProfileSerializer
	queryset = UserProfile.objects.all()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (UpdateOwnProfile,)
	filter_backends = (filters.SearchFilter,)
	search_fields = ('email','name',)



class UserLoginApiView(ObtainAuthToken):

	renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES




class ProfileFeedViewSet(viewsets.ModelViewSet):

	serializer_class = ProfilefeedSerializer
	queryset = ProfileFeedItem.objects.all()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (UpdateOwnStatus,IsAuthenticatedOrReadOnly)


	def perform_create(self , serializer):

		serializer.save(user_profile=self.request.user)




	