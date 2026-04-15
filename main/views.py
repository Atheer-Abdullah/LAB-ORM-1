from django.shortcuts import render, redirect
from blog.models import Post 

# دالة الصفحة الرئيسية 
def home_view(request):
    posts = Post.objects.all().order_by('-published_at')
    return render(request, "main/home.html", {"posts": posts})

# دالة إضافة منشور جديد
def add_post_view(request):
    if request.method == "POST":
        
        print("FILES RECEIVED:", request.FILES) 
        
        new_post = Post(
            title=request.POST.get("title"),
            content=request.POST.get("content"),
            poster=request.FILES.get("poster"), 
            media=request.FILES.get("media"),   
            video=request.FILES.get("video")    
        )
        new_post.save() 
        
        return redirect("main:home_view") 
    
    return render(request, "blog/add_post.html")
    return redirect("main:home_view")