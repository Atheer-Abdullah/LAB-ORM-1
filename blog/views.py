from django.shortcuts import render
from .models import Post

# (دالة إضافة المنشور )
def add_post_view(request):
    if request.method == "POST":
       
        new_post = Post(
            title=request.POST["title"],
            content=request.POST["content"]
        )
        new_post.save()
        return render(request, "blog/add_post.html") 
    
    return render(request, "blog/add_post.html")


def home_view(request):
    posts = Post.objects.all()
    return render(request, "main/home.html", {"posts": posts})

def post_detail_view(request:HttpRequest, post_id:int):
    post = Post.objects.get(pk=post_id)
    return render(request, "blog/post_detail.html", {"post": post})