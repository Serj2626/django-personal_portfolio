from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    '''function to display all blogs'''
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


def all_detail(request, blog_id):
    '''function to display blog by id'''
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
