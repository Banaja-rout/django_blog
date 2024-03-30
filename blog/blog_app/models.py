from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Blog(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,null=False)
	title = models.CharField(max_length=100,null=False)
	content = models.TextField()
	publish_date = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
	media = models.FileField(default=None)
	views = models.BigIntegerField(default=0)
	

	def total_likes(self):
		return self.likes.count()
   
