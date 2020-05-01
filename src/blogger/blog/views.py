from django.shortcuts import render

# fake posts for test
posts = [
    {
        'title':'Learn Django 3',
        'content':'Leran how to create app web with django 3 '
    },
        {
        'title':'Learn Laravel 7',
        'content':'Leran how to create app web with Laravel 7 '
    },
        {
        'title':'Learn Angular 8',
        'content':'Leran how to create app web with Angular 8 '
    },
        {
        'title':'Learn React',
        'content':'Leran how to create app web with React '
    },
]
# Create your views here.
def home(request):
    context = {
        'title' : 'Home',
        'posts' : posts,
    }
    return render(request,'blog/index.html',context);
