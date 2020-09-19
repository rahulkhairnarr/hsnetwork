from django.shortcuts import render
from userprofile.models import Contacts
from posts.models import Post
from posts.serializers import PostSerializer, CreatePostSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from django.db.models import Q

User = get_user_model()


class PostListView(generics.ListAPIView):
    model = Post
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        # Get Current User
        user = self.request.user

        # Get User Interest
        user_interest = user.profile.user_interest.all()

        # Get User List of Following
        user_following = Contacts.objects.values_list('following', flat=True).filter(user=user)

        print(user_following)

        # Filter All Post based on Following
        post_list = self.model.objects.filter(user__in=user_following).distinct()

        # Return 
        return post_list

class PostView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        # Get Current User
        user = request.user

        # Create Post Instance
        post = Post(user=user)

        # Create PostSerializer Instance
        post_serializer = CreatePostSerializer(post, data=request.data)

        # Check Validation
        if post_serializer.is_valid():
            # Save Model
            post_serializer.save()

            # Return Model
            return Response(post_serializer.data, status=status.HTTP_201_CREATED)

        # Return Error
        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)