from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register_views, name = 'register'),
    path('login/', views.login_views, name = 'login'),
    path('logout/', views.logout_views, name = 'logout'),
    
]
