from django.urls import path
from blog import views

app_name = 'blog'


urlpatterns = [
    path('create/', views.create_blog_post, name = 'post-create'),
    path('list/', views.blog_post_list, name = 'post-list'),
    path('detail/<slug:slug>/', views.blog_post_detail, name = 'post-detail'),
    path('update/<slug:slug>/', views.update_blog_post, name = 'post-update'),
    path('delete/<slug:slug>/', views.delete_blog_post, name = 'post-delete'),
    path('comment/<slug:slug>/', views.add_comment, name = 'post-comment'),
    path('comment/delete/<int:comment_id>/', views.remove_comment, name = 'remove-comment'),
    path('comment/edit/<int:comment_id>/', views.edit_comment, name = 'edit-comment'),
]





