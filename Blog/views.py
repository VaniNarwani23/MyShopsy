from django.shortcuts import render

from .models import BlogPost
# Create your views here.
def index(request):
    myposts = BlogPost.objects.all()
    print(myposts)
    return render(request, 'Blog/index.html', {'myposts':myposts})
def blogpost(request,id):
    post = BlogPost.objects.filter(post_id = id) [0]
    print(post)
    return render(request, 'Blog/blogpost.html', {'post':post})
# Create your views here.