from django.shortcuts import render
from .models import Post


# Create your views here.

def index(request):
    posts = Post.objects.all()

    context = {
        "posts" : posts
    }
    return render(request, "app_blog/index.html", context)





