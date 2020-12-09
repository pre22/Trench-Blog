from django.contrib import admin
from blogs.models import ContactModel, Post, CategoryTable, Comment


class CommentInline(admin.TabularInline):
    model = Comment


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(ContactModel)
admin.site.register(CategoryTable)
admin.site.register(Comment)
