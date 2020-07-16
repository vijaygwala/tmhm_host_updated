from rest_framework import serializers
from myauth.models import *
from django.contrib.auth import get_user_model
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email','first_name','last_name')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ( 'first_name', 'last_name', 'email', 'password' )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(validated_data['email'], validated_data['password'])

        return user