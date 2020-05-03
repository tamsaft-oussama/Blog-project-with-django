from django.shortcuts import render
from .models import Post
# Create your views here.
def home(request):
    context = {
        'title' : 'Home',
        'posts' : Post.objects.all(),
    }
    return render(request,'blog/index.html',context);

def about(request):
    return render(request,'blog/about.html',{'title':'About Me'})

def post_details(request,post_id):
    context = {
        'title' : 'Post Details',
        'post' : Post.objects.get(pk=post_id)
    }
    return render(request,'blog/details.html',context)
