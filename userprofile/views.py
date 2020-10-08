from django.shortcuts import render
from userprofile.models import Interest, UserProfile, Contacts
from userprofile.serializers import InterestSerializer, UserProfileSerializer, CreateUserProfileSerializer, ContactsSerializer, SuggestedPeople
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from django.db.models import Q


User = get_user_model()


# Create your views here.

class InterestView(generics.ListCreateAPIView):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = LimitOffsetPagination


class UserProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        # Get User from Token
        user = request.user

        try:
            # Try to get User Profile
            profile = UserProfile.objects.get(user=user)

            # Serialize Data
            profile_serializer = UserProfileSerializer(profile)

            # Return Response
            return Response(profile_serializer.data, status=status.HTTP_200_OK)
        except UserProfile.DoesNotExist:
            raise NotFound(detail="User Profile doesn't exist")

    def post(self, request):
        # Get User from Token
        user = request.user

        # Create Instance of User Profile
        profile = UserProfile(user=user)

        # Serialize Data
        profile_serializer = CreateUserProfileSerializer(profile, data=request.data)
        
        # Check User Data is valid or not
        if profile_serializer.is_valid():
            # Save Data to Model
            profile_serializer.save()

            # Response User with serialize data
            return Response(profile_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PeopleSuggestion(generics.ListAPIView):
    model = User
    serializer_class = SuggestedPeople
    permission_classes = (IsAuthenticated,)
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        # Get Current User
        user = self.request.user

        # Get User Interest
        user_interest = user.profile.user_interest.all()

        # Get User List of Following
        user_following = Contacts.objects.values_list('following', flat=True).filter(user=user)

        # Filter All User based on Interest
        user_list = self.model.objects.filter(profile__user_interest__in=user_interest).exclude(Q(id__in=user_following) | Q( username=user)).distinct()

        # Return 
        return user_list


class AddFollower(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        # Get User
        user = request.user

        # Check user already following
        is_following = Contacts.objects.filter(user=user, following=request.data['following']).exists()

        if is_following:
            # Response with allready following message
            return Response({"detail": "Already following"}, status=status.HTTP_400_BAD_REQUEST)
        # If user not following
        else:
            # Create Instance of Contact
            contact = Contacts(user=user)
            
            # Create Instance of serializer and pass data to serializer
            contact_serializer = ContactsSerializer(contact, data=request.data)

            # Check validation
            if contact_serializer.is_valid():
                # Save Data
                contact_serializer.save()

                # Return Serializer Resonse
                return Response(contact_serializer.data, status=status.HTTP_201_CREATED)

            # Return Error 
            else:
                # Return Serializes Error Response
                return Response(contact_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetFollowingList(generics.ListAPIView):
    model = User
    serializer_class = SuggestedPeople
    permission_classes = (IsAuthenticated,)
    pagination_class = LimitOffsetPagination
    lookup_field = ['id']

    def get_queryset(self):
        # Get Current User
        user = self.request.user

        # Get User Interest
        user_interest = user.profile.user_interest.all()

        # Get User List of Following
        user_following = Contacts.objects.values_list('following', flat=True).filter(user=user)

        # Filter All User based on Interest
        user_list = self.model.objects.filter(id__in=user_following).distinct()

        # Return 
        return user_list


