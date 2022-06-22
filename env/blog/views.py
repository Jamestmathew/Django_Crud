from audioop import reverse
from django.urls import reverse_lazy
from django.views.generic.edit import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DetailView
from django.views.generic.edit import UpdateView
from .models import Post


class PostListView(ListView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    filds = "__all__"
    success_url: reverse_lazy("blog:all")


class PostDetailView(DetailView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url: reverse_lazy("blog:all")


class PostDeleteView(UpdateView):
    model = Post
    fields = "__all__"
    success_url: reverse_lazy("blog:all")