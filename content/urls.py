from django.urls import path
from . import views

urlpatterns = [
    path("home/<str:username>",views.homepage , name="home"),
    path("get_content/<str:username>",views.getting_content,name="Getpost"),
    path("likedislike/<int:id>/<str:curruser>",views.like_dislike,name="like"),
    path("profile/<str:username>",views.profilepage,name="profile"),
    path("followbutton",views.working_of_follow_button,name="flwbuttn") ,
    path("followers_following/<str:username>",views.getting_follower_page,name="f_f"),
    path("rmove",views.removinguser,name="remove"),
    path("deletepost",views.deleting_from_profilepage,name="delete"),
    path("getcomment/<int:postid>/<str:username>",views.getting_comments,name="comment"),
    path("addcomment/<int:postid>",views.adding_comments,name="addcomment")
    
]