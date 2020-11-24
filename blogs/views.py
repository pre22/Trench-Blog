from django.views.generic import ListView, TemplateView, CreateView, UpdateView
from blogs.models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'blogs/index.html'
