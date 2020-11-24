from django.urls import  path
from blogs.views import BlogListView, AboutPageView, ContactPageView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
]
