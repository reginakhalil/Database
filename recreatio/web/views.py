from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'web/home.html', context)


class PostListView(ListView): 
    model = Post
    template_name = 'web/home.html' 
    context_object_name = 'posts'
    ordering = ['-date_posted'] #orders posts from newest to oldest

class PostDetailView(DetailView): 
    model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView): 
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form): 
        form.instance.author = self.request.user #set the author of the post to the user currently logged in 
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form): 
        form.instance.author = self.request.user #set the author of the post to the user currently logged in 
        return super().form_valid(form)

    #this function is to make sure that only the author of a post is able to make updates 
    def test_func(self): 
        post = self.get_object()
        #check if the user currenlty logged in is the author of the post
        return self.request.user == post.author

#delete a post 
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): 
    model = Post
    success_url = '/'
   #this function is to make sure that only the author of a post is able to make updates 
    def test_func(self): 
        post = self.get_object()
        #check if the user currenlty logged in is the author of the post
        return self.request.user == post.author

def about(request):
    return render(request, 'web/about.html', {'title': 'About'})

def login(request):
    return render(request, 'web/login.html', {'title': 'Login'})

