from django.urls import  path
from blogs.views import (
    BlogListView, 
    AboutPageView, 
    ContactPageView, 
    BlogCreateView,
    BlogDetailView,
    BlogUpdateView,
    BlogDeleteView,
    ProfilePage,
    ProfilePageUpdate,
    CreateCommentView,
)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/new', login_required(BlogCreateView.as_view()), name='post_new'),
    path('post/<int:pk>/edit/', login_required(BlogUpdateView.as_view()), name='post_edit'),
    path('post/<int:pk>/delete/', login_required(BlogDeleteView.as_view()), name='post_delete'),
    path('post/<int:pk>/comment/', CreateCommentView.as_view(), name="comment"),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('dashboard/<int:pk>/', login_required(ProfilePage.as_view()), name='profile'),
    # path('profile/<int:pk>/', login_required(ProfilePage.as_view()), name="profile"),
    path('profile/<int:pk>/update/', login_required(ProfilePageUpdate.as_view()), name="profile_update"),
    
]
