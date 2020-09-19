from django.urls import path
from userprofile import views


app_name = 'userprofile'

urlpatterns = [
    path('interest/', views.InterestView.as_view(), name="interest"),
    path('userprofile/', views.UserProfileView.as_view(), name="user_profile"),
    path('people-suggestion/', views.PeopleSuggestion.as_view(), name="people-suggestion"),
    path('follow/', views.AddFollower.as_view(), name="follow"),
    path('get-following-list/', views.GetFollowingList.as_view(), name='following-list'),
]
