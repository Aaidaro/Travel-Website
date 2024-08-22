from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    tag = models.ManyToManyField(Tag)
    category = models.ManyToManyField(Category)
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_date"]

    def __str__(self) -> str:
        return f"{self.title}-{self.id}"
    
    def get_published_posts():
        published_posts = Post.objects.filter(status= 1, published_date__lte= timezone.now())
        return published_posts
    
    
    def get_next_id(self, current_object_id):
        next_post = Post.objects.filter(id__gt=current_object_id, status= 1,
                    published_date__lte= timezone.now()).order_by('id').only('id').first()
        if next_post:
            return next_post
        else:
            return None
        
    def get_previous_id(self, current_object_id):
        previous_post = Post.objects.filter(id__lt=current_object_id, status= 1,
                        published_date__lte= timezone.now()).order_by('-id').only('id').first()
        if previous_post:
            return previous_post
        else:
            return None