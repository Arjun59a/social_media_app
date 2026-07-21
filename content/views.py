from django.shortcuts import render,redirect,get_object_or_404
from .models import Post,Postlike,Profile,follower_list
from django.contrib.auth import get_user_model


User = get_user_model()
def getting_content(request,username) :
    if request.method == 'POST' :
        title1 = request.POST.get('title')
        Discription = request.POST.get('description')
        image1 = request.FILES.get('image')

        un = get_object_or_404(User,username=username)

        Post.objects.create(
            user = un,
            image = image1,
            title = title1,
            description = Discription
        )

        return redirect("home_app:home",username=username)



       

   
    return render(request,"addpost.html",{'username':username})

def homepage(request,username) :
    dt = Post.objects.all()
    context = {
        'data': dt,
        'username': username  
    }
    
    return render(request,"home.html",context=context)



def like_dislike(request,id,curruser) :
   
    curruser_obj = User.objects.get(username=curruser)
    post_details = Post.objects.get(id=id)
    
    if not Postlike.objects.filter(user=curruser_obj,title = post_details).exists() :
        Postlike.objects.create(
            user = curruser_obj ,
            title = post_details
        )
    pst_obj = Postlike.objects.get(user=curruser_obj , title = post_details)

    if not pst_obj.liked :
        pst_obj.liked = True
        post_details.likes += 1
    else :
        pst_obj.liked = False
        post_details.likes -= 1
    
    
    pst_obj.save()
    post_details.save()

    return redirect(request.META.get("HTTP_REFERER", "/"))


def profilepage(request,username) :
    user_obj = get_object_or_404(User,username=username)
    followerno = follower_list.objects.filter(following = user_obj)
    followingno = follower_list.objects.filter(follower = user_obj)
    curr_profile,created = Profile.objects.get_or_create(user=user_obj)
    if request.method == 'POST' :
        imageurl = request.FILES.get('image')
        bio = request.POST.get('bio')
        print(imageurl)
        print(bio)
        curr_profile.profilepic=imageurl
        curr_profile.bio=bio
        curr_profile.save()
        return redirect("home_app:home",username=username)
    post_obj = Post.objects.filter(user=user_obj)
    context = {
        'posts' :post_obj,
        'profile' :curr_profile,
        'username' : username , 
        'followers' : followerno.count(),
        'follower_obj' : followerno , 
        'following' : followingno.count(),
        'following_obj' : followingno


    }
    return render(request,"profilepage.html",context=context)


def working_of_follow_button(request) :
    username = request.session.get("username")
    followeruser  = get_object_or_404(User,username=username)

    if request.method == 'POST' :
        user = request.POST['userid']
        followinguser = get_object_or_404(User,username = user)
        if followinguser != followeruser :
            if not follower_list.objects.filter(follower = followeruser,following = followinguser).exists() :
                follower_list.objects.create(
                    follower = followeruser,
                    following = followinguser
                )
            else :
                obj = get_object_or_404(follower_list,follower = followeruser,following = followinguser)
                obj.delete()
            
        return redirect(request.META.get("HTTP_REFERER", "/"))
    

def getting_follower_page(request) :
    pass


        
    


   
    



