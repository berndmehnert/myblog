from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Post
from django.views import View
from .forms import PostForm

class PostCreateView(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'blog/post_form.html', {'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Redirect to the post list after saving
        return render(request, 'blog/post_form.html', {'form': form})

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
