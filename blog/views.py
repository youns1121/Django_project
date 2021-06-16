from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
# Create your views here.



def index(request):
    post_infos = Post.objects.all()
    return render(request, 'index.html', context={'posts':post_infos})

def single_post_page(request, pk):
    post_info = Post.objects.get(pk=pk)

    return render(request, 'single_post_page.html', context={'post':post_info})

class PostDetail(DetailView):
    model = Post
    template_name = 'cbv_detail.html'

class PostList(ListView):
    model = Post
    template_name = 'cbv_index.html'

class NewPostList(ListView):
    model = Post
    template_name = 'bt_blog_list.html'




