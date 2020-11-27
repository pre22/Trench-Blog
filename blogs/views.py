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
from django.contrib.auth.mixins import UserPassesTestMixin

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
    fields = ['title', 'category', 'body']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdateView(UpdateView, UserPassesTestMixin):
    model = Post
    template_name = 'blogs/post_edit.html'
    fields = ['title', 'body']
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class BlogDeleteView(DeleteView, UserPassesTestMixin):
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

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

# class ContactPageView(FormView):
#     form_class = ContactForm
#     template_name = 'blogs/contact.html'
#     success_url = reverse_lazy('home')
