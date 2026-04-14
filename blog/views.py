from django.shortcuts import render, redirect, get_object_or_404 # أضفنا get_object_or_404 هنا
from .models import Post

# دالة إضافة المنشور
def add_post_view(request):
    if request.method == "POST":
        new_post = Post(
            title=request.POST["title"],
            content=request.POST["content"],
            is_published=request.POST.get("is_published", True)
        )
        new_post.save()
        return redirect("main:home_view")
    
    return render(request, "blog/add_post.html")

