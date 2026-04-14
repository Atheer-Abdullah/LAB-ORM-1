from django.shortcuts import render, redirect
from .models import Post 

def add_post_view(request):
    if request.method == "POST":
        new_post = Post(
            title=request.POST["title"],
            content=request.POST["content"]
        )
        new_post.save()
        
        return redirect("main:home_view") 

    return render(request, "blog/add_post.html")