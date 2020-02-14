from rest_framework import serializers
from .models import UserProfile , ProfileFeedItem




class ProfileSerializer(serializers.ModelSerializer):

	class Meta:

		model = UserProfile
		fields = ('id' , 'email' , 'name' , 'password')
		extra_kwargs = {'password':
		{'write_only':True , 'style':{
		'input_type':'password'}
		}
		}



	def create(self , validated_data):
		user = UserProfile.objects.create_user(
			email=validated_data['email'],
			name=validated_data['name'],
			password=validated_data['password']
			)

		return user




class ProfilefeedSerializer(serializers.ModelSerializer):

	class Meta:

		model = ProfileFeedItem
		fields = ('user_profile' , '_created_on' , 'status_text')

		extra_kwargs = {'user_profile':{'read_only':True}}