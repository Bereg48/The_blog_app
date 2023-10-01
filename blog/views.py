from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    """Метод post_list принимает request, извлекает все посты со статусом PUBLISHED, используя менеджер published"""
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, id):
    """Метод post_detail принимает аргумент  id поста, извлекает объект Post с заданным id
    , вызывает метод  get_object_or_404()"""

    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/detail.html', {'post': post})



