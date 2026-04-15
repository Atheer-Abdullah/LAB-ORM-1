from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('add/', views.add_post_view, name='add_post_view'),
    path("detail/<post_id>/", views.post_detail_view, name="post_detail_view"),
    path("post/update/<post_id>/", views.post_update_view, name="post_update_view"),
    path("post/delete/<post_id>/", views.post_delete_view, name="post_delete_view"),
]