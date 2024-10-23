from django.db import models
from auth_app.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=100000)
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='category', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    snippet = models.TextField()
    body = models.TextField()

    class Meta:
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name="blog", on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    body = models.TextField()

    def __str__(self):
        return self.blog.title