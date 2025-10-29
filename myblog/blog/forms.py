from blog.models import BlogPost, PostComment
from django import forms

class CreateBlogPost(forms.ModelForm):
    
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image', 'video', 'document', 'status',]
        
        
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = PostComment
        fields = ['comment_content']
        
