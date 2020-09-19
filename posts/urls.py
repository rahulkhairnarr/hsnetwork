from django.urls import path
from posts import views

app_name = 'post'

urlpatterns = [
    path('all-post/', views.PostListView.as_view(), name="post_list"),
    path('post/', views.PostView.as_view(), name='create_post')
]
