from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm
from .models import UserProfile


# Create your views here.
def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			# form.cleaned_data is a dictionary with values in request.POST
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"An account was created for {username}!")
			return redirect('login')

	else:
		form = RegistrationForm()
	return render(request, 'users/register.html', {'form':form})
@login_required	
def profile(request):
	print(request.user.email)
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST,instance=request.user)
		p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.userprofile)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, "Yay 😊😊 your profile has been updated successfully")
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.userprofile)


	
	context = {
		'u_form':u_form, 'p_form':p_form
	}
	return render(request, 'users/profile.html',context)
