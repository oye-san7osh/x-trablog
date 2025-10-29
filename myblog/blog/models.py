from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.
    
class PublishedManager(models.Manager):
    def get_queryset(self):
        return(
            super().get_queryset().filter(status=BlogPost.PostStatus.PUBLISHED)
        )


# Blog Post Model
class BlogPost(models.Model):
    
    class PostStatus(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
        
    
    title = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255)
    content = models.TextField()
    
    
    # for uploading images, videosm & attachments
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    document = models.FileField(upload_to='attachments/', blank=True, null=True)
    
    
    published_date = models.DateTimeField(default = timezone.now)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    slug = models.SlugField(max_length = 500, unique=True)
    status = models.CharField(
        max_length = 2,
        choices = PostStatus,
        default = PostStatus.DRAFT
    )
    
    
    objects = models.Manager()
    published_post = PublishedManager()
    
    # indexing 
    class Meta:
        ordering = ['-published_date']
        indexes = [
            models.Index(fields=['-published_date'])
        ]
    
    # for generating the slug link
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            num = 1
            while BlogPost.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num +=1
            self.slug = slug
        super().save(*args, **kwargs)
        
    
    
    def __str__(self):
        return self.title
    
    
    
    
class PostComment(models.Model):
    
    post = models.ForeignKey(BlogPost, on_delete = models.CASCADE, related_name="comments")
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default = True)
    
    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["-created_at"])
        ]
    
    

    