from django.db import models
from django.contrib.auth.models import User

class Post(models.Model) :
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    image= models.ImageField(upload_to="posts/")
    title = models.CharField(max_length=200)
    description = models.TextField()
    likes = models.IntegerField(default=0)
    

class Postlike(models.Model) :
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.ForeignKey(Post,on_delete=models.CASCADE)
    liked = models.BooleanField(default=False)
   