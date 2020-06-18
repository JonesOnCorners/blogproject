from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import request
from blog.models import Post
from blog.decoraters import my_login_required

# Create your views here.

@login_required
def index(request):
    post = Post.objects.all()
    context = {'title':'Home',
               'posts' :post
               }

    return render(request, 'blog/index.html',context)
