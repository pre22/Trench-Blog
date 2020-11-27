from django.views.generic import (
    ListView, 
    TemplateView, 
    CreateView, 
    FormView, 
    DetailView, 
    UpdateView,
    DeleteView,
)
from blogs.models import Post
from blogs.forms import ContactForm
from django.urls import reverse_lazy
from blogs.models import ContactModel

class BlogListView(ListView):
    paginate_by = 10
    model = Post
    template_name = 'blogs/index.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blogs/post.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'blogs/post_new.html'
    fields = ['title', 'author', 'category', 'body']
    success_url = reverse_lazy('home')

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blogs/post_edit.html'
    fields = ['title', 'body']
    success_url = reverse_lazy('home')

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blogs/post_delete.html'
    success_url = reverse_lazy('home')

class AboutPageView(TemplateView):
    template_name = 'blogs/about.html'

class ContactPageView(CreateView):
    model = ContactModel
    template_name = 'blogs/contact.html'
    fields = ['name', 'email', 'phone', 'message']
    success_url = reverse_lazy('home')

# class ContactPageView(FormView):
#     form_class = ContactForm
#     template_name = 'blogs/contact.html'
#     success_url = reverse_lazy('home')
