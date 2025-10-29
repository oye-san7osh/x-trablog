from django.shortcuts import get_object_or_404, render, redirect
from blog.models import BlogPost, PostComment
from blog.forms import CreateBlogPost, CommentForm
from django.contrib.auth.decorators import login_required



# create your views here


def create_blog_post(request):
    
    if request.method == 'POST':
        create_post = CreateBlogPost(request.POST, request.FILES)
        
        if create_post.is_valid():
            post = create_post.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:post-list')
    else:
        create_post = CreateBlogPost()
    return render(request,
                  'blog/blog-post-create.html',
                  {'postcreate': create_post})
    
    
@login_required(login_url='users:login')
def blog_post_list(request):
    post = BlogPost.published_post.all()
    return render(request,
                  'blog/blog-list.html',
                  {'postlist': post})
    

def blog_post_detail(request, slug):
    postdetail = get_object_or_404(
        BlogPost,
        slug = slug,
        status = BlogPost.PostStatus.PUBLISHED,
    )
    comments = postdetail.comments.filter(is_active = True)
    
    return render(request,
                  'blog/blog-detail.html',
                  {'postdetail': postdetail,
                   "comments": comments})
    
    
def update_blog_post(request, slug):
    post = get_object_or_404(BlogPost, slug = slug)
    
    if request.method == 'POST':
        form = CreateBlogPost(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:post-detail', slug= post.slug)
    else:
        form = CreateBlogPost(instance=post)
    
    return render(request,
                  'blog/update-blog-post.html',
                  {'form': form})
    
    
def delete_blog_post(request, slug):
    post = get_object_or_404(
        BlogPost,
        slug=slug,
        status = BlogPost.PostStatus.PUBLISHED,
    )
    
    if request.method == "POST":
        post.delete()
        return redirect('blog:post-list')
    
    return render(request,
                  'blog/delete-blog-post.html',
                  {'post':post})
    
 
@login_required(login_url = 'user:login')  
def add_comment(request, slug):
    post = get_object_or_404(BlogPost, slug = slug)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('blog:post-detail', slug=post.slug)
    else:
        form = CommentForm()
        
    return render(request,
                  'blog/comment-post.html',
                  {"commentForm": form,
                  "post": post})
    
    
    
@login_required
def remove_comment(request, comment_id):
    comment = get_object_or_404(PostComment, id=comment_id)
    
    comment.delete()
    
    return redirect('blog:post-detail', slug=comment.post.slug)


@login_required
def edit_comment(request, comment_id):
    
    comment = get_object_or_404(PostComment, id=comment_id)
    
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        
        if form.is_valid():
            form.save()
            
            return redirect('blog:post-detail', slug=comment.post.slug)
        
    else:
        form = CommentForm(instance=comment)
        
    return render(request, 'blog/edit-comment.html', {'form': form, 'comment':comment})
    
    
    
    
    
    
            
        

    
            
        
