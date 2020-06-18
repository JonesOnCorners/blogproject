from django.shortcuts import render
from django.http import request
from blog.models import Post

# Create your views here.

def index(request):
    post = Post.objects.all()
    context = {'title':'Home',
               'posts' :post
               }

    return render(request, 'blog/index.html',context)
