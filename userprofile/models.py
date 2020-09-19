from django.db import models
from django.contrib.auth import get_user_model

# Get Current Active User Model
User = get_user_model()


class Interest(models.Model):
    interest_id = models.AutoField(primary_key=True)
    interest_name = models.CharField(max_length=100)

    def __str__(self):
        return self.interest_name

# Create your models here.
class UserProfile(models.Model):
    """Generate UserProfile which stores User Bio and Interest. User interest can be used to suggest people.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    about_us = models.TextField(help_text="User short bio")
    user_interest = models.ManyToManyField(Interest, related_name='interest')


    def __str__(self):
        return self.user.username


class Contacts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")

    def __str__(self):
        return self.user.username


