from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .models import Post

# دالة إضافة المنشور
def add_post_view(request: HttpRequest):
    if request.method == "POST":
        new_post = Post(
            title=request.POST["title"],
            content=request.POST["content"],
            
            poster=request.FILES.get("poster") 
        )
        new_post.save()
        return redirect("main:home_view") # يفضل الرديركت بعد الحفظ
    
    return render(request, "blog/add_post.html")

# الصفحة الرئيسية
def home_view(request: HttpRequest):
    posts = Post.objects.all().order_by("-published_at")
    return render(request, "main/home.html", {"posts": posts})

# صفحة التفاصيل البحث بالـ ID
def post_detail_view(request: HttpRequest, post_id: int):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "blog/post_detail.html", {"post": post})

# صفحة التعديل
def post_update_view(request: HttpRequest, post_id: int):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        post.title = request.POST.get("title", post.title)
        post.content = request.POST.get("content", post.content)
        
        
        if "poster" in request.FILES:
            post.poster = request.FILES["poster"]
        
        if "video" in request.FILES:
            post.video = request.FILES["video"]

        if "media" in request.FILES:
            post.media = request.FILES["media"]

        post.save()
        
        return redirect("blog:post_detail_view", post_id=post.id)

    return render(request, "blog/post_update.html", {"post": post})