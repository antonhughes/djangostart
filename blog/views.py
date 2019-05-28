from django.shortcuts import render
from .models import Post
from django.utils import timezone


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    namesoflakes = {'Lake 1': "Lagan", 'Lake 2': "Windsor", 'Lake 3': "Windy"}

    return render(request, 'blog/post_list.html', {'posts': posts, 'lakes': namesoflakes})
