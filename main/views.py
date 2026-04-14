from django.shortcuts import render

from blog.models import Post 

def home_view(request):
    
    posts = Post.objects.all().order_by('-published_at')
    return render(request, "main/home.html", {"posts": posts})