from django.shortcuts import render
from .models import Blog


def all_blogs(request):
    '''function to display all blogs'''
    blogs = Blog.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


def all_detail(request, blog_id):
    '''function to display blog by id'''
    return render(request, 'blog/detail.html', {'id': blog_id})
