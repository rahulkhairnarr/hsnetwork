from userprofile.models import UserProfile, Interest, Contacts
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class InterestSerializer(serializers.ModelSerializer):
    """InterestSerializer use to serialized Interest model
    """

    class Meta:
        model = Interest
        fields = '__all__'


class CreateUserProfileSerializer(serializers.ModelSerializer):
    """UserProfileSerializer use to make serialized UserProfile Data
    """
    class Meta:
        model = UserProfile
        exclude = ['user']

class UserProfileSerializer(serializers.ModelSerializer):
    """UserProfileSerializer use to make serialized UserProfile Data
    """
    class Meta:
        model = UserProfile
        fields = '__all__'


class ContactsSerializer(serializers.ModelSerializer):
    """ContactsSerializer used to serializer Contact Data
    """

    class Meta:
        model = Contacts
        exclude = ['user']

class SuggestedPeople(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name','last_name', 'username']