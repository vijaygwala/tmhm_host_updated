from rest_framework import serializers
from myauth.models import *
from django.contrib.auth import get_user_model
from facilitators.models import *
from LandingPage.models import *
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email','first_name','last_name')

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['Linkedin_Url', 'Website_Url', 'Youtube_Url','RExperience','TExperience']
   
class FacilitatorQueriesForm(serializers.ModelSerializer):
    class Meta:
        model=FacilitatorQueries
        fields=('query',)
   



# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ( 'first_name', 'last_name', 'email', 'password' )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(validated_data['email'], validated_data['password'])

        return user