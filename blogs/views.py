from django.views.generic import ListView, TemplateView, CreateView, FormView
from blogs.models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'blogs/index.html'

class AboutPageView(TemplateView):
    model = Post
    template_name = 'blogs/about.html'

class ContactPageView(FormView):
    model = Post
    template_name = 'blogs/contact.html'

class PostPageView(CreateView):
    model = Post
    template_name = 'blogs/post.html'