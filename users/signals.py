from django.db.models.signals import post_save
from .models import UserProfile
# from django.dispatch import receiver
from django.contrib.auth.models import User

# Creating a new user profile object with an instance of our extended user model
# instance is an instance of User
def createProfile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)
post_save.connect(createProfile, sender=User)

# Saving the newly created user profile
def saveProfile(sender,instance, **kwargs):
	instance.userprofile.save()
post_save.connect(saveProfile, sender=User)

