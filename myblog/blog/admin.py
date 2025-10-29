from django.contrib import admin
from blog.models import BlogPost


# Register your models here.
@admin.register(BlogPost)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_date', 'status', 'slug',]
    list_filter = ['status', 'created', 'published_date', 'author',]
    search_fields = ['title', 'author', 'content', 'status']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status', 'published_date']
    show_facets = admin.ShowFacets.ALWAYS
    
    