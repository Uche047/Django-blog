from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.http import HttpResponse
from django.views import generic
from .models import *

# Create your views here

def home(request):
	context = {"posts":Post.objects.all()}
	return render(request,'blog/home.html',context)

class PostListView(generic.ListView):
	#model = Post
	queryset = Post.objects.order_by('-pk')
	paginate_by = 5
	template_name = 'blog/home.html'
	#ordering = ['-pk']
	#context_object_name = 'posts'
	def get_queryset(self,*args, **kwargs):
		search = self.request.GET.get('search')
		if search:
			return Post.objects.filter(title__icontains=search).order_by('-pk')
			
		return Post.objects.all().order_by('-pk')
	


class UserPostListView(generic.ListView):
	paginate_by = 5
	template_name = 'blog/user_posts.html'
	#context_object_name = 'posts'

	
	def get_queryset(self,*args, **kwargs):
		user = get_object_or_404(User, username=self.kwargs['username'])
		search = self.request.GET.get('search')
		if True:
			if search:
				return Post.objects.filter(title__icontains=search).order_by('-pk')
			return Post.objects.filter(author=user).order_by('-pk')
	



class PostDetailView(generic.DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin,generic.CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,generic.UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		print(self.get_object())

		if self.get_object().author == self.request.user:
			return True
		return False
		
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,generic.DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		if self.get_object().author == self.request.user:
			return True
		return False

def about(request):
	return render(request,'blog/about.html', {"title":"About"})