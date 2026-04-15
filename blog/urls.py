from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('add/', views.add_post_view, name='add_post_view'),
    path("detail/<post_id>/", views.post_detail_view, name="post_detail_view"),
]