from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):

    posts = Blog.objects.order_by('-date')[:5]

    return render(request, 'blog/all_blogs.html', {'posts': posts})

def detail(request, post_id):

    post = get_object_or_404(Blog, pk=post_id)

    return render(request, 'blog/detail.html', {'post':post})