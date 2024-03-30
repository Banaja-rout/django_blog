from django.urls import path
from .views import *

urlpatterns = [
	

    path('', home, name='home'),
    path('blogs/', blog_list, name='blog_list'),
    path('blogs/<int:pk>/', blog_detail, name='blog_detail'),
    path('blogs/create/', create_blog, name='create_blog'),
    path('blogs/<int:pk>/edit/', edit_blog, name='edit_blog'),
    path('blogs/<int:pk>/delete/', delete_blog, name='delete_blog'),
    # urls.py
    path('blog/<int:pk>/like/', like_blog, name='like_blog'),

    path('signup/', signup_page, name='signup'),
    path('login/', login_page, name='login'),
    path('logout/', user_logout, name='logout'),

    ]
