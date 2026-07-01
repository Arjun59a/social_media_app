from django.urls import path
from . import views

urlpatterns = [
    path("home/<str:username>",views.homepage , name="home"),
    path("get_content/<str:username>",views.getting_content,name="Getpost"),
    path("likedislike/<int:id>/<str:curruser>",views.like_dislike,name="like")
]