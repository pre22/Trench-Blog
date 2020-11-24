from django.views.generic import ListView, TemplateView, CreateView, FormView
from blogs.models import Post
from blogs.forms import ContactForm

class BlogListView(ListView):
    model = Post
    template_name = 'blogs/index.html'

class AboutPageView(TemplateView):
    model = Post
    template_name = 'blogs/about.html'

class ContactPageView(FormView):
    form_class = ContactForm
    template_name = 'blogs/contact.html'
    success_url = 'contact'

class PostPageView(CreateView):
    model = Post
    template_name = 'blogs/post.html'