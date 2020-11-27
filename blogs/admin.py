from django.contrib import admin
from blogs.models import ContactModel, Post, CategoryTable

admin.site.register(Post)
admin.site.register(ContactModel)
admin.site.register(CategoryTable)