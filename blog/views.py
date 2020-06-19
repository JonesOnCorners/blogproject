from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import request
from blog.models import Post
from blog.decoraters import my_login_required
from django.views.generic import( 
                                  CreateView
                                 ,ListView
                                 ,DetailView
                                 ,UpdateView
                                 ,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

@login_required
def index(request):
    post = Post.objects.all()
    context = {'title':'Home',
               'posts' :post
               }

    return render(request, 'blog/index.html',context)


class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return True if self.request.user == post.author else False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'    

    def test_func(self):
        post = self.get_object()
        return True if self.request.user == post.author else False