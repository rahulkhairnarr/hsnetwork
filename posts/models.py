from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Post(models.Model):
    """Post model is used to post made by User
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post")
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username