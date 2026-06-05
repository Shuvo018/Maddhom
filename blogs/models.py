from pyclbr import Class

from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='author_user')
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return self.first_name

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return self.category_name

STATUS_CHOICES = (
    ("Draft", "Draft"),
    ("Published", "Published")
)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    short_description = models.CharField(max_length=500)
    blog_body = models.TextField(max_length=2000)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default='Draft')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='user_comments')
    blog = models.ForeignKey(to=Blog, on_delete=models.CASCADE, related_name='post_comments')
    content = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE,blank=True, null=True, related_name='child_comment')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.content


