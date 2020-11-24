from django.urls import  path
from blogs.views import BlogListView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
]
