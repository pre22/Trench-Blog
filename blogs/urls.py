from django.urls import  path
from blogs.views import (
    BlogListView, 
    AboutPageView, 
    ContactPageView, 
    BlogCreateView,
    BlogDetailView,
    BlogUpdateView,
    BlogDeleteView,
)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/new', login_required(BlogCreateView.as_view()), name='post_new'),
    path('post/<int:pk>/edit/', login_required(BlogUpdateView.as_view()), name='post_edit'),
    path('post/<int:pk>/delete/', login_required(BlogDeleteView.as_view()), name='post_delete'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
]
