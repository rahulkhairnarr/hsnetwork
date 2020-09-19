from django.contrib import admin
from userprofile.models import UserProfile, Interest, Contacts

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Interest)
admin.site.register(Contacts)