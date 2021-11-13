from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class RegistrationForm(UserCreationForm):
	email = forms.EmailField()

	class Meta():
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta():
		model = User
		# We want to update just the username and email 
		fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta():
		model = UserProfile
		fields = ['image']